from otree.api import *
import random
import pandas
import json

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    observational_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                      'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                                      'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                          'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                      'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                      'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
                          'twolinks': {'x': [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                                       'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                          'collider': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                                       'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}}

    interventional_data = 0     # пока не уверен в правильности интервенции не стал ничего писать

    task_sequence = (list(observational_data.keys()))
    random.shuffle(task_sequence)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField()

# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number
    target_vocabulary = C.task_sequence[num_round]




# PAGES
class MyPage(Page):
    pass


class DiagramTaskCopy(Page):
    def live_method(player, data):
        # player.stored = str(1)
        player.stored = json.dumps(data)

    @staticmethod
    def vars_for_template(player):
        return dict(
            '''
            onelinkx=C.observational_data['onelink']['x'],
            onelinky=C.observational_data['onelink']['y'],
            onelinkz=C.observational_data['onelink']['z'],
            nolinksx=C.observational_data['nolinks']['x'],
            nolinky=C.observational_data['nolinks']['y'],
            nolinksz=C.observational_data['nolinks']['z'],
            twolinksx=C.observational_data['twolinks']['x'],
            twolinksy=C.observational_data['twolinks']['y'],
            twolinksz=C.observational_data['twolinks']['z'],
            colliderx=C.observational_data['collider']['x'],
            collidery=C.observational_data['collider']['y'],
            colliderz=C.observational_data['collider']['z'],
            '''
        )



class DiagramTest(Page):

    @staticmethod
    def js_vars(player):
        store_array = json.loads(player.stored)
        return dict(
            nodes=[
                {'data': {'counter': 0, 'id': 'X', 'name': 'X', }, 'style': {'background-color': '#c3cec0'}},
                {'data': {'counter': 0, 'id': 'Y', 'name': 'Y', }, 'style': {'background-color': '#c3cec0'}},
                {'data': {'counter': 0, 'id': 'Z', 'name': 'Z', }, 'style': {'background-color': '#c3cec0'}},
            ],
            edges=store_array,
            edges_original=[
                {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},

            ]
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [DiagramTaskCopy, DiagramTest, ResultsWaitPage, Results]
