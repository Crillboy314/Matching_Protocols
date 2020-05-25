from ._builtin import Page, WaitPage
from otree.api import Currency as c
from .models import Constants

import random


class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'fee': self.session.config["participation_fee"],
        }

class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return {
            'rate': self.session.config["real_world_currency_per_point"],
        }


class Cutoff(Page):
    form_model = 'player'
    form_fields = ['cutoff']

    def vars_for_template(self):
        return {
            'both_h': self.player.create_matrix()['A']['A'],
            'hd_payoff': self.player.create_matrix()['A']['B'],
            'dh_payoff': self.player.create_matrix()['B']['A'],
            'dd_payoff': self.player.create_matrix()['B']['B'],
            'mu_pay': self.session.config["mu_pay"]
        }


class CutWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_strategies()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()

        self.group.set_cumpay()


class Results(Page):
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        players = self.subsession.get_players()

        return {
            'my_decision': self.player.decision,
            'my_cutoff': self.player.cutoff,
            'my_privatepi': self.player.private_payoff,
            'temp_A': range(self.subsession.round_number, 1, -1),
            'oneshot': self.session.config["seque"] == 0,
            'nooneshot': self.session.config["seque"] > 0,
            'twonightplayers': self.group.count_noche == 2,
            'other_player_decision': self.player.other_player().decision,
            'same_choice': self.player.decision == self.player.other_player().decision,
            'player_in_all_rounds': player_in_all_rounds,
            'payoff_otro': self.player.other_player().payoff,
            'round_number': self.subsession.round_number
        }


class Adios(Page):
    form_model = 'player'
    form_fields = ['gender']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Pagos(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'pago_final': self.participant.payoff,
            'pago_COL': self.participant.payoff_plus_participation_fee()
        }


class Trial(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.payoff = 0
        self.player.dummy_decision = self.player.decision


page_sequence = [
    Welcome,
    Instructions,
    Cutoff,
    CutWaitPage,
    ResultsWaitPage,
    Results,
    Trial,
    Pagos,
]
