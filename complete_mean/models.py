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
    name_in_url = 'com_mean'
    players_per_group = 2
    num_rounds = 11

    betray_payoff = c(60)
    betrayed_payoff = c(5)

    both_cooperate_payoff = c(100)
    both_defect_payoff = c(50)




class Subsession(BaseSubsession):
    totalA = models.IntegerField()
    totalB = models.IntegerField()
    average = models.CurrencyField(initial=0)

    """Mezcla aleatoriamente cada ronda"""
    def creating_session(self):
        self.group_randomly()

    def counting_H(self):
        totalAt = 0
        totalBt = 0

        for p in self.get_players():
            if p.decision == "B":
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
        self.average = 0
        for p in self.get_players():
            self.average += p.payoff
        self.average = self.average / len(self.get_players())
        return self.average

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices = ['A', 'B'],
        doc = """Decisión del jugador actual""",
        widget = widgets.RadioSelect()
    )

    dummy_decision = models.CharField(choices=['A', 'B'],
                                         doc="dum decision"
                                         )

    def other_player(self):
        return self.get_others_in_group()[0]

    def create_matrix(self):
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

        return points_matrix


    def set_payoff(self):
        self.payoff = c(self.create_matrix()[self.decision]['A'] * self.session.vars['weight_matrix'][self.decision]['A'] + self.create_matrix()[self.decision]['B']* self.session.vars['weight_matrix'][self.decision]['B'])

    def get_coop(self):
        """Devuelve el número de colaboraciones hasta la ronda anterior."""
        num_coop = 0
        for p in self.in_previous_rounds():
            if p.decision=="B":
                num_coop+=1
        return num_coop
