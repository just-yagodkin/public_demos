from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'trains'
    players_per_group = None
    num_rounds = 5
    speed= 0.01


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    difficulty = models.IntegerField()
    task = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
