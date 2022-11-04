from otree.api import *
import json


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'any_app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField()

# functions
def live_method(player, data):
    # player.stored = str(1)
    player.stored = json.dumps(data)

# PAGES
class MyPage(Page):
    live_method = live_method


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(player):
        store_array = json.loads(player.stored)
        
        return {'edges':[(i,v["id"], v['label']) for i,v in enumerate(store_array)]}


page_sequence = [MyPage, ResultsWaitPage, Results]
