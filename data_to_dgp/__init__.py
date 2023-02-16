from otree.api import *
import goodfunctions as gf
import random
import json

doc = """
Your app description
"""


# test 123
class C(BaseConstants):
    TEST = True
    if not TEST:
        NUM_ROUNDS = 2
    else:
        NUM_ROUNDS = 5

    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None

    data_edges = {'nolinks': [False],
                  'onelink': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}],
                  'twolinks': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                  'collider1': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}],
                  'fork': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YX', 'source': 'Y', 'target': 'X', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                  'collider2': [
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}]
                  }

    preobservational_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                         'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                                         'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                             'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                         'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                         'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
                             'twolinks': {'x': [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                                          'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                          'z': [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]},
                             'collider1': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                           'y': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                           'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
                             'fork': {'x': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                                      'y': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                      'z': [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]},
                             'collider2': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                                           'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                                           'z': [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1]}
                             }  # collider2 is optional

    preinterventional_data = {'nolinks':    gf.intervente('nolinks', preobservational_data['nolinks']),
                              'onelink':    gf.intervente('onelink', preobservational_data['onelink']),
                              'twolinks':   gf.intervente('twolinks', preobservational_data['twolinks']),
                              'collider1':  gf.intervente('collider', preobservational_data['collider1']),
                              'fork':       gf.intervente('fork', preobservational_data['fork']),
                              'collider2':  gf.intervente('collider', preobservational_data['collider2'])
                              }
    '''                                                 

    def reshuffle(initialdict):
        new_dict = initialdict.copy()

        lenght = 16
        new_dict=initialdict.copy()

        keys_level_1 = list(initialdict.keys())
        # works with warning and only if use xyz names always!!!
        keys_level_2 = list(initialdict[list(initialdict.keys())[0]].keys())

        seq = random.sample(list(range(16)), lenght)
        for key in keys_level_1:
            for key_second in keys_level_2:
                new_dict[key][key_second] = random.sample(initialdict[key][key_second],
                                                           len(initialdict[key][key_second]))
                new_dict[key][key_second] = [initialdict[key][key_second][seq[i]] for i in  range(lenght) ]
    '''


    #observational_data = reshuffle(preobservational_data)
    #interventional_data = reshuffle(preinterventional_data)

    observational_data = gf.reshuffle(preobservational_data)
    interventional_data = gf.reshuffle(preinterventional_data)

    task_sequence_keys = (list(observational_data.keys()))
    if not TEST:
        task_sequence = random.sample(task_sequence_keys, len(task_sequence_keys))
    else:
        task_sequence = ['collider1', 'twolinks', 'collider2', 'fork', 'onelink' ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField(initial=json.dumps(
        [{"data": {"counter": 0, "id": "X", "name": "X"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Y", "name": "Y"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Z", "name": "Z"}, "style": {"background-color": "#c3cec0"}}]))
    trainig = models.IntegerField()


# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    target_vocabulary = [C.observational_data[target_key], C.interventional_data[target_key]]
    return target_vocabulary


def benchmark_diagram(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    target_vocabulary = C.data_edges[target_key]
    return target_vocabulary


'''
def check_diagram(players_data: dict, original_data: dict):
    Сравнивает диаграмму игрока и диаграмму датасета, выдает None, если игрок указал всё верно; либо набор лишних и нехвативших связей, если что-то оказалось неверным
    if players_data == original_data:
        return None
    dif_list = []
    for data in players_data:  # записываем лишнее
        if data in original_data:
            pass
        else:
            dif_list.append(data)
    for data in original_data:  # записываем недостающее
        if data in players_data:
            pass
        else:
            dif_list.append(data)
    return dif_list
'''


# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Training(Page):
    form_model = 'player'
    form_fields = ['trainig']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    def live_method(player, data):
        player.trainig = json.loads(json.dumps(data))[0]["counter"]
        return {1: player.trainig}
        # json.loads(player.trainig)[0]["counter"]

    # def trainig_error_message(player, value):
    #     if value != 1:
    #         return 'Wrong answer'

    def error_message(player, values):
        solutions = dict(
            trainig=1,
        )
        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'incorrect report'
        return error_messages


class DiagramTask(Page):

    def live_method(player, data):
        # player.stored = str(1)
        player.stored = json.dumps(data)

    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        return dict(
            datasetobs=[(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in
                        range(len(output[0]['x']))],
            datasetint=[(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in
                        range(len(output[1]['x']))],
            frequenciesobs=["frequencies"] + gf.check_frequencies(output[0]),
            frequenciesint=["frequencies"] + gf.check_frequencies(output[1]))


class DiagramTest(Page):
    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        if C.TEST:
            return dict(
                ekey=[C.task_sequence, C.task_sequence_keys, benchmark_diagram(player)[0]])
        else:
            return

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


page_sequence = [Instruction, Training, DiagramTask, DiagramTest]
