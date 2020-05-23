from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        return{
            'other_player_num_coop': self.player.other_player().get_coop,
            'num_prev_round': self.subsession.round_number-1,
        }


class ResultsWaitPage(WaitPage):

    body_text = 'Espera a que el oponente decida'

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        self.player.set_payoff()

        return{
            'my_decision': self.player.decision.upper(),
            'other_player_decision': self.player.other_player().decision.upper(),
            'payoff_otro': self.player.other_player().payoff,
            'round_number': self.subsession.round_number,
            'same_choice': self.player.decision == self.player.other_player().decision,
        }

class Pagos(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'pago_final': self.participant.payoff,
            'pago_USD': self.participant.payoff_plus_participation_fee()
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
    Decision,
    ResultsWaitPage,
    Results,
    Trial,
    Pagos
]
