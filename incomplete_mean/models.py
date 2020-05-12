from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

import random

doc = """


"""


class Constants(BaseConstants):
    name_in_url = 'inc_mean'
    players_per_group = 2
    num_rounds = 11


class Subsession(BaseSubsession):
    totalA = models.IntegerField()
    totalB = models.IntegerField()

    average = models.CurrencyField(initial=0)

    def creating_session(self):

        self.group_randomly()

        for p in self.get_players():
            p.private_payoff = c(random.randint(0, self.session.config["bothd_payoff"]))

    def counting_H(self):
        totalAt = 0
        totalBt = 0

        for p in self.get_players():
            if p.private_payoff < p.cutoff:
                totalBt = totalBt + 1
            else:
                totalAt = totalAt + 1


        self.totalA = totalAt
        self.totalB = totalBt

        self.create_matrix()

        for p in self.get_players():
            p.set_payoff()

        self.session.vars['avg'] = self.get_average()


    def create_matrix(self):
        n = len(self.get_players())
        t_payoff_matrix = {
            'A':
                {
                    'A': (self.totalA - 1)/(n-1),
                    'B': (self.totalB )/(n-1)
                },
            'B':
                {
                    'A': (self.totalA  )/(n-1),
                    'B': (self.totalB - 1)/(n-1)
                }
        }

        self.session.vars['weight_matrix'] = t_payoff_matrix

    def get_average(self):
        for p in self.get_players():
            self.average += p.payoff
        self.average = self.average / len(self.get_players())
        return self.average


class Group(BaseGroup):

    def set_strategies(self):

        for p in self.get_players():
            if p.private_payoff < p.cutoff:
                p.decision = 'B'
            else:
                p.decision = 'A'


class Player(BasePlayer):
    gender = models.CharField(
        choices=['femenino', 'masculino'],
        doc="genero",
        widget=widgets.RadioSelect()
    )



    cutoff = models.CurrencyField(
        min=0, max=100 + 1,
        doc="min H payoff which player plays H",
        initial=0
    )

    decision = models.CharField(
        choices=['A', 'B'],
        doc="""Players play""",
        widget=widgets.RadioSelect()
    )

    private_payoff = models.CurrencyField(
        doc="H payoff",
        initial=0
    )

    dummy_decision = models.CharField(choices=['A', 'B'],
                                         doc="dum decision"
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
        self.payoff = c(self.create_matrix()[self.decision]['A']
                        * self.session.vars['weight_matrix'][self.decision]['A'] +
                        self.create_matrix()[self.decision]['B']
                        * self.session.vars['weight_matrix'][self.decision]['B'])
