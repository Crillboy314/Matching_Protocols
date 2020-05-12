from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Cutoff, {"cutoff": c(99)})
        yield (pages.Moves, {"move": 'Dia'})
        assert self.player.private_payoff == c(99)
        assert self.player.whomoves == 1
        assert self.player.payoff == c(99)
        assert self.player.decision == 'B'
        assert self.player.cum_payoff  == c(100)
        yield (pages.Results)
