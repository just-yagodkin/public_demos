from otree.api import *
import goodfunctions as gf
import random
import json

doc = """
Your app description
"""


# test 123
class C(BaseConstants):
    NUM_ROUNDS = 6

    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None

    NOLINKSSEED = random.randint(0, 5)
    ONELINKSEED = random.randint(0, 5)
    TWOLINKSSEED = random.randint(0, 5)
    COLLIDER1SEED = random.randint(0, 5)
    FORKSEED = random.randint(0, 5)
    COLLIDER2SEED = random.randint(0, 5)
    THREELINKSSEED = random.randint(0, 5)

    seed = {'collider1': COLLIDER1SEED,
            'nolinks': NOLINKSSEED,
            'onelink': ONELINKSEED,
            'twolinks': TWOLINKSSEED,
            'fork': FORKSEED,
            'collider2': COLLIDER2SEED,
            'threelinks': THREELINKSSEED
            }

    data_edges = {'nolinks': [False],
                  'onelink': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}],
                      ONELINKSEED),
                  'twolinks': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                      TWOLINKSSEED),
                  'collider1': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}],
                      COLLIDER1SEED),
                  'fork': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YX', 'source': 'Y', 'target': 'X', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}],
                      FORKSEED),
                  'collider2': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}],
                      COLLIDER2SEED),
                  'threelinks': gf.smartedgesinterv([
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YX', 'source': 'Y', 'target': 'X', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},
                      {'data': {'counter': 0, 'weight': 0, 'id': 'XZ', 'source': 'X', 'target': 'Z', 'label': ""}}],
                      THREELINKSSEED)
                  }

    preobservational_data = {'nolinks': gf.smartdatainterv({'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                            'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                                                            'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                                                           NOLINKSSEED),
                             'onelink': gf.smartdatainterv({'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                            'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                                            'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
                                                           ONELINKSEED),
                             'twolinks': gf.smartdatainterv({'x': [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                                                             'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                             'z': [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]},
                                                            TWOLINKSSEED),
                             'collider1': gf.smartdatainterv({'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                              'y': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                              'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
                                                             COLLIDER1SEED),
                             'fork': gf.smartdatainterv({'x': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                                                         'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         'z': [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]},
                                                        FORKSEED),
                             'threelinks': gf.smartdatainterv({'x': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                                         'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                                                        THREELINKSSEED)
                             #  'collider2': gf.smartdatainterv({'x': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                             #                'y': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                             #                'z': [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1]}, COLLIDER2SEED)
                             }  # collider2 is optional

    preinterventional_data = {
        'nolinks': gf.smartdatainterv(gf.intervente('nolinks', preobservational_data['nolinks']), NOLINKSSEED),
        'onelink': gf.smartdatainterv(gf.intervente('onelink', preobservational_data['onelink']), ONELINKSEED),
        'twolinks': gf.smartdatainterv(gf.intervente('twolinks', preobservational_data['twolinks']), TWOLINKSSEED),
        'collider1': gf.smartdatainterv(gf.intervente('collider', preobservational_data['collider1']), COLLIDER1SEED),
        'fork': gf.smartdatainterv(gf.intervente('fork', preobservational_data['fork']), FORKSEED),
        'threelinks': gf.smartdatainterv(gf.intervente('threelinks', preobservational_data['threelinks']), THREELINKSSEED)
        # 'collider2': gf.smartdatainterv(gf.intervente('collider', preobservational_data['collider2']), COLLIDER2SEED)
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

    observational_data = gf.reshuffle(preobservational_data)
    interventional_data = gf.reshuffle(preinterventional_data)

    task_sequence_keys = (list(observational_data.keys()))

    task_sequence = random.sample(task_sequence_keys, len(task_sequence_keys))
    # task_sequence = ['onelink', 'twolinks', 'collider1', "nolinks"]

    SEEDS = []  # SEEDS contains seed for every round

    for i in task_sequence:
        SEEDS.append(seed[i])

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


# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def js_vars(player):
        return dict(
            num_rounds=C.NUM_ROUNDS)


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
                error_messages[field_name] = 'Incorrect report'
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
            # frequenciesobs=gf.check_frequencies(output[0]),
            frequenciesint=["frequencies"] + gf.check_frequencies(output[1]))

    @staticmethod
    def js_vars(player):
        output = datatask_output_json(player)
        return dict(
            datasetobs=[(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in
                        range(len(output[0]['x']))],
            datasetint=[(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in
                        range(len(output[1]['x']))],
            frequenciesobs=["frequencies"] + gf.check_frequencies(output[0]),
            # frequenciesobs=gf.check_frequencies(output[0]),
            frequenciesint=["frequencies"] + gf.check_frequencies(output[1]),
            seed=C.SEEDS[player.round_number - 1])


class DiagramTest(Page):
    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        store_array = json.loads(player.stored)
        seed = C.SEEDS[player.round_number - 1]
        edges = C.data_edges
        return dict(
            ekey=[C.task_sequence, gf.tanc(store_array), seed])

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
