from otree.api import *
import random
import pandas
import json

doc = """
Your app description
"""

# test
class C(BaseConstants):
    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField()


# PAGES
class MyPage(Page):
    pass

class DiagramTask(Page):
    def live_method(player, data):
    # player.stored = str(1)
        player.stored = json.dumps(data)

class DiagramTest(Page):
    
    @staticmethod
    def js_vars(player):
        store_array = json.loads(player.stored)
        return dict(
    nodes= [
      { 'data': {'counter':0, 'id': 'X', 'name': 'X', },  'style': { 'background-color': '#c3cec0' }},
      { 'data': {'counter':0, 'id': 'Y', 'name': 'Y', },  'style': { 'background-color': '#c3cec0' }},
      { 'data': {'counter':0, 'id': 'Z', 'name': 'Z', },  'style': { 'background-color': '#c3cec0' }},
    ],
    edges= store_array,
    edges_original  = [
      { 'data': {'counter':0, 'weight':0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""} },
      { 'data': {'counter':0, 'weight':0, 'id': 'YZ', 'source': 'Y', 'target': 'Z' , 'label': ""} },

    ]
        )


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [DiagramTask, DiagramTest, ResultsWaitPage, Results]
