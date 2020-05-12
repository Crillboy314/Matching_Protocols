from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Hola'

doc = """
Continuous Prisoner's Dilemma (random partner, 5 rounds)
"""


class Constants(BaseConstants):
    name_in_url = 'com_ran'
    players_per_group = 2
    num_rounds = 11

    betray_payoff = c(60)
    betrayed_payoff = c(5)

    both_cooperate_payoff = c(100)
    both_defect_payoff = c(50)




class Subsession(BaseSubsession):
    """Mezcla aleatoriamente cada ronda"""
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices = ['B', 'A'],
        doc = """Decisión del jugador actual""",
        widget = widgets.RadioSelect()
    )

    dummy_decision = models.CharField(choices=['A', 'B'],
                                         doc="dum decision"
                                         )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        points_matrix = {
            'B': {
                'B': Constants.both_cooperate_payoff,
                'A': Constants.betrayed_payoff
            },
            'A': {
                'B': Constants.betray_payoff,
                'A': Constants.both_defect_payoff
            }
        }

        self.payoff = (points_matrix[self.decision][self.other_player().decision])

    def get_coop(self):
        """Devuelve el número de colaboraciones hasta la ronda anterior."""
        num_coop = 0
        for p in self.in_previous_rounds():
            if p.decision=="B":
                num_coop+=1
        return num_coop
