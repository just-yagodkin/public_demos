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
    NUM_ROUNDS = 2

    data_edges = {'nolinks': [False],
                  'onelink': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}],
                  'twolinks': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                  'collider': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}]}

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

    interventional_data = 0  # пока не уверен в правильности интервенции не стал ничего писать

    task_sequence_keys = (list(observational_data.keys()))
    # task_sequence = random.choices(task_sequence_keys, k=len(task_sequence_keys))
    task_sequence = random.sample(task_sequence_keys, len(task_sequence_keys))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField()


# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    target_vocabulary = C.observational_data[target_key]
    return target_vocabulary


def benchmark_diagram(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    target_vocabulary = C.data_edges[target_key]
    return target_vocabulary


# PAGES
class MyPage(Page):
    pass


class DiagramTaskCopy(Page):
    def live_method(player, data):
        # player.stored = str(1)
        player.stored = json.dumps(data)

    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        return dict(
            dataset=[(output['x'][i], output['y'][i], output['z'][i]) for i in range(len(output['x']))])


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


class DiagramTest(Page):
    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        return dict(
            ekey=[C.task_sequence, C.task_sequence_keys, benchmark_diagram(player)[0]])

    @staticmethod
    def js_vars(player):
        benchmark_edges = benchmark_diagram(player)

        store_array = json.loads(player.stored)
        show_edges = 0
        if benchmark_edges[0]:
            show_edges = 1
        else:
            show_edges = 0

        return dict(
            nodes=[
                {'data': {'counter': 0, 'id': 'X', 'name': 'X', }, 'style': {'background-color': '#c3cec0'}},
                {'data': {'counter': 0, 'id': 'Y', 'name': 'Y', }, 'style': {'background-color': '#c3cec0'}},
                {'data': {'counter': 0, 'id': 'Z', 'name': 'Z', }, 'style': {'background-color': '#c3cec0'}},
            ],
            edges=store_array,
            edges_original=benchmark_edges,
            show_edges_template=show_edges
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [DiagramTaskCopy, DiagramTest, Results]
