from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player

class DifficultyChoice(Page):
    form_model = 'player'
    form_fields = ['difficulty']


class Task(Page):
    form_model = 'player'
    form_fields = ['task']
    

    def before_next_page(self):
            self.player.payoff = self.player.difficulty*self.player.task


class Results(Page):
    pass


page_sequence = [
    DifficultyChoice,
    Task,
    Results
]
