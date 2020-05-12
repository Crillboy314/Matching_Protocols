from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

import random

doc = """

"""


class Constants(BaseConstants):
    name_in_url = 'inc_rand'
    players_per_group = 2
    num_rounds = 11


class Subsession(BaseSubsession):

    def creating_session(self):

        self.group_randomly()

        for p in self.get_players():
            p.private_payoff = random.randint(0, self.session.config["bothd_payoff"])
        for g in self.get_groups():
            g.randn = random.randint(1, 2)


class Group(BaseGroup):
    randn = models.IntegerField()
    count_noche = models.IntegerField()

    def set_strategies(self):

        for p in self.get_players():
            if p.private_payoff < p.cutoff:
                p.decision = 'B'
            else:
                p.decision = 'A'

    def set_payoff(self):

        for p in self.get_players():
            p.set_payoff()

    def set_cumpay(self):
        for p in self.get_players():
            p.cum_payoff = sum([j.payoff for j in p.in_all_rounds()])


class Player(BasePlayer):
    gender = models.CharField(
        choices=['femenino', 'masculino'],
        doc="genero",
        widget=widgets.RadioSelect()
    )

    cutoff = models.CurrencyField(
        min=0, max=100 + 1,
        doc="min H payoff which player plays H"
    )

    decision = models.CharField(
        choices=['A', 'B'],
        doc="""Players play""",
        widget=widgets.RadioSelect()
    )

    dummy_decision = models.CharField(
        choices=['A', 'B'],
        doc="""trial decision"""
    )

    private_payoff = models.CurrencyField(
        null=True,
        doc="H payoff"
    )

    cum_payoff = models.CurrencyField(
        null=True,
        doc="cum payoff"
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def create_matrix(self):
        payoff_matrix = {
            'A':
                {
                    'A': self.private_payoff,
                    'B': self.private_payoff + c(self.session.config["mu_pay"])
                },
            'B':
                {
                    'A': c(self.session.config["d_payoff"]),
                    'B': c(self.session.config["bothd_payoff"])
                }
        }

        return payoff_matrix

    def set_payoff(self):
        self.payoff = self.create_matrix()[self.decision][self.other_player().decision]
