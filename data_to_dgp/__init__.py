from otree.api import *
import goodfunctions as gf
import random
import json
import ast

doc = """
Your app description
"""


class C(BaseConstants):
    training = False
    Bonus = 5
    Round_payoff = 10
    NUM_ROUNDS = 8
    SHOWING_INFORMATION_EDGE = 0.51  # you will see a feedback only after this percent of rounds

    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None

    conf_range = range(101)

    task_sequence = ['twolinks', 'onelink', 'collider1', "threelinks", "fork", "threelinks", "nolinks", 'onelink']

    # task_sequence = ["nolinks", 'onelink', 'twolinks', 'collider1', "fork", "threelinks", "nolinks", 'onelink',
    #                  'twolinks', 'collider1', "threelinks", "fork"]

    # task_sequence = ["nolinks", 'onelink']

    seed = [(name, random.randint(0, 5)) for name in task_sequence]
    # seed = [(name, 2) for name in task_sequence]
    # print(seed)

    pre_data_edges = {'nolinks': [False],
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
                      'threelinks': [
                          {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
                          {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},
                          {'data': {'counter': 0, 'weight': 0, 'id': 'XZ', 'source': 'X', 'target': 'Z', 'label': ""}}],
                      }

    a = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}], seed[0][1])

    b = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}], seed[1][1])

    c = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'ZY', 'source': 'Z', 'target': 'Y', 'label': ""}}], seed[2][1])

    d = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'XZ', 'source': 'X', 'target': 'Z', 'label': ""}}], seed[3][1])

    e = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'YX', 'source': 'Y', 'target': 'X', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}}], seed[4][1])

    f = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'YZ', 'source': 'Y', 'target': 'Z', 'label': ""}},
        {'data': {'counter': 0, 'weight': 0, 'id': 'XZ', 'source': 'X', 'target': 'Z', 'label': ""}}], seed[5][1])

    g = gf.smartedgesinterv([False], seed[6][1])

    h = gf.smartedgesinterv([
        {'data': {'counter': 0, 'weight': 0, 'id': 'XY', 'source': 'X', 'target': 'Y', 'label': ""}}], seed[7][1])

    data_edges = [a, b, c, d, e, f, g, h]
    #print(data_edges)

    original_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
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
                     'threelinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'y': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                    'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
                     }

    pre_preobservational_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
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
                                 'threelinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                'y': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                                'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
                                 }
    preobservational_data = [[x[0], gf.smartdatainterv(gf.pre_preobservational_data[x[0]], x[1])] for x in seed]

    # X -> Y ->
    # |       |
    # |       V
    # ▶  ->  Z

    preinterventional_data = [[x[0], gf.smartdatainterv(gf.intervente(x[0], gf.original_data[x[0]]), x[1])] for x in
                              seed]

    # preinterventionalx_data = {  # INTERVENTION ON X
    #     'nolinks': gf.smartdatainterv(gf.intervente('nolinks', original_data['nolinks'], 'x'), NOLINKSSEED),
    #     'onelink': gf.smartdatainterv(gf.intervente('onelink', original_data['onelink'], 'x'), ONELINKSEED),
    #     'twolinks': gf.smartdatainterv(gf.intervente('twolinks', original_data['twolinks'], 'x'), TWOLINKSSEED),
    #     'collider1': gf.smartdatainterv(gf.intervente('collider', original_data['collider1'], 'x'),
    #                                     COLLIDER1SEED),
    #     'fork': gf.smartdatainterv(gf.intervente('fork', original_data['fork'], 'x'), FORKSEED),
    #     'threelinks': gf.smartdatainterv(gf.intervente('threelinks', original_data['threelinks'], 'x'),
    #                                      THREELINKSSEED)
    # }

    # preinterventionalz_data = {  # INTERVENTION ON Z
    #     'nolinks': gf.smartdatainterv(gf.intervente('nolinks', original_data['nolinks'], 'z'), NOLINKSSEED),
    #     'onelink': gf.smartdatainterv(gf.intervente('onelink', original_data['onelink'], 'z'), ONELINKSEED),
    #     'twolinks': gf.smartdatainterv(gf.intervente('twolinks', original_data['twolinks'], 'z'), TWOLINKSSEED),
    #     'collider1': gf.smartdatainterv(gf.intervente('collider', original_data['collider1'], 'z'),
    #                                     COLLIDER1SEED),
    #     'fork': gf.smartdatainterv(gf.intervente('fork', original_data['fork'], 'z'), FORKSEED),
    #     'threelinks': gf.smartdatainterv(gf.intervente('threelinks', original_data['threelinks'], 'z'),
    #                                      THREELINKSSEED)
    # }

    if len(task_sequence) < NUM_ROUNDS:
        NUM_ROUNDS = len(task_sequence)

    edge = NUM_ROUNDS * SHOWING_INFORMATION_EDGE

    observational_data = gf.reshuffle(preobservational_data)

    interventional_data = gf.reshuffle(preinterventional_data)
    # interventionalx_data = gf.reshuffle(preinterventionalx_data)
    # interventionalz_data = gf.reshuffle(preinterventionalz_data)

    # SOMETIMES YOU DONT WANT THE DATA TO BE SHUFFLED => UNCOMMENT THE STRINGS BELOW

    # observational_data = preobservational_data
    # interventional_data = preinterventional_data
    # interventionalx_data = preinterventionalx_data
    # interventionalz_data = preinterventionalz_data

    # IF YOU DONT WANT ROUNDS TO BE SHUFFLED, UNCOMMENT THE STRING BELOW

    # task_sequence = random.sample(task_sequence_keys, len(task_sequence_keys))
    # task_sequence = ["nolinks", 'onelink', 'twolinks', 'collider1', "fork", "threelinks", "nolinks", 'onelink', 'twolinks', 'collider1', "fork", "threelinks"]
    # task_sequence = ['threelinks']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stored = models.StringField(initial=json.dumps(
        [{"data": {"counter": 0, "id": "X", "name": "X"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Y", "name": "Y"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Z", "name": "Z"}, "style": {"background-color": "#c3cec0"}}]))

    training = models.IntegerField()

    conf_bid = models.IntegerField(initial=-1,
                                   choices=[i for i in C.conf_range],
                                   # widget=widgets.RadioSelect,
                                   )

    buttons = models.StringField()

    buttons_before_err = models.StringField()

    score = models.FloatField(initial=0)

    accuracy = models.FloatField()

    cycle_err = models.IntegerField(initial=1)

    def conf_bid_error_message(player, value):
        print('value is', value)
        return 'not an option'

    feedback = models.StringField(label="Любая обратная связь")

    Aot_1 = models.IntegerField(
        min=1, max=5,
        choices=[1, 2, 3, 4, 5],
        label='Сегодня хорошая погода',
        widget=widgets.RadioSelectHorizontal)

    Aot_2 = models.IntegerField(
        min=1, max=5,
        choices=[1, 2, 3, 4, 5],
        label='Вы хорошо себя чувствуете',
        widget=widgets.RadioSelectHorizontal)

    Aot_3 = models.IntegerField(
        min=1, max=5,
        choices=[1, 2, 3, 4, 5],
        label='Вам нравится проводить время на свежем воздухе',
        widget=widgets.RadioSelectHorizontal)


# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    target_vocabulary = [C.observational_data[num_round][1], C.interventional_data[num_round][1],
                         #  C.interventionalx_data[target_key],
                         #  C.interventionalz_data[target_key]
                         ]
    return target_vocabulary


def benchmark_diagram(player: Player):
    num_round = player.round_number - 1
    # target_key = C.task_sequence[num_round]
    target_vocabulary = C.data_edges[num_round]
    #print(C.data_edges)
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
    form_fields = ['training']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    def live_method(player, data):
        newdata = [data[0]["counter"], data[1]["counter"], data[2]["counter"], data[3]["counter"], data[4]["counter"],
                   data[5]["counter"]]  ###
        # 0pos: X -> Y
        # 1pos: Y -> X
        # 2pos: Y -> Z
        # 3pos: X -> Z
        # 4pos: Z -> Y
        # 5pos: Z -> X

        player.training = int((newdata == [1, 0, 0, 0, 0, 0]))  ###  int(TRUE) if X -> Y
        return {1: player.training}

    def error_message(player, values):
        solutions = dict(
            training=1,
        )
        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Форма заполнена неверно'
        return error_messages


class DiagramTask(Page):
    form_model = 'player'
    form_fields = ['conf_bid', 'stored', 'buttons']

    def live_method(player, data):
        player.stored = json.dumps(data)
        return {1: player.stored}

    def error_message(player, values):

        values['stored'] = gf.tanc(player.stored)
        solutions = dict(
            stored=True,
            conf_bid=values['conf_bid'],
            buttons=values['buttons']
        )

        # print(solutions)

        player.accuracy = round(
            gf.accuracy(gf.fine(gf.userschoice(player.stored), gf.dgpchoice(benchmark_diagram(player)))), 12)

        player.score = 1 - round((values['conf_bid'] * 0.01 - player.accuracy) ** 2, 5)

        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'В форме присутствует цикл'
                player.stored = '[{"counter": 0, "weight": 0, "id": "XY", "source": "X", "target": "Y", "label": ""}, ' \
                                '{"counter": 0, "weight": 0, "id": "YX", "source": "Y", "target": "X", "label": ""}, ' \
                                '{"counter": 0, "weight": 0, "id": "YZ", "source": "Y", "target": "Z", "label": ""}, ' \
                                '{"counter": 0, "weight": 0, "id": "XZ", "source": "X", "target": "Z", "label": ""}, ' \
                                '{"counter": 0, "weight": 0, "id": "ZY", "source": "Z", "target": "Y", "label": ""}, ' \
                                '{"counter": 0, "weight": 0, "id": "ZX", "source": "Z", "target": "X", "label": ""}]'
                if player.cycle_err:
                    player.buttons_before_err = values['buttons']
                player.cycle_err = 0

        store_array = player.stored
        edges = benchmark_diagram(player)
        accuracy = round(gf.accuracy(gf.fine(gf.userschoice(store_array), gf.dgpchoice(edges))), 4)
        player.payoff = cu(round(player.score, 5) * C.Bonus + accuracy * C.Round_payoff)

        return error_messages

    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)

        return dict(
            datasetobs=[(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in
                        range(len(output[0]['x']))],
            datasetint=[(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in
                        range(len(output[1]['x']))],
            frequenciesobs=["freq"] + gf.check_frequencies(output[0]),
            frequenciesint=["freq"] + gf.check_frequencies(output[1]),

        )

    @staticmethod
    def js_vars(player):

        output = datatask_output_json(player)
        return dict(
            datasetobs=[(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in
                        range(len(output[0]['x']))],
            datasetint=[(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in
                        range(len(output[1]['x']))],
            frequenciesobs=["freq"] + gf.check_frequencies(output[0]),
            frequenciesint=["freq"] + gf.check_frequencies(output[1]),
            seed=C.seed[player.round_number - 1][1],
        )


class DiagramTest(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number >= C.edge

    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)
        store_array = player.stored
        seed = C.seed[player.round_number - 1][1]
        edges = benchmark_diagram(player)
        #print(edges)
        datasetobs = C.observational_data[player.round_number - 1][1]
        datasetint = C.interventional_data[player.round_number - 1][1],
        buttons_were_clicked = json.loads(player.buttons)
        # datasetintx = C.interventionalx_data[C.task_sequence[player.round_number - 1]],
        # datasetintz = C.interventionalz_data[C.task_sequence[player.round_number - 1]]

        accuracy = round(gf.accuracy(gf.fine(gf.userschoice(store_array), gf.dgpchoice(edges))), 4)
        player.payoff = cu(round(player.score, 5) * C.Bonus + accuracy * C.Round_payoff)

        return dict(
            ekey=[f'The original sequence is {C.task_sequence}',
                  f'User did not set cycles: {gf.tanc(store_array)}',
                  f'User chose {gf.userschoice(store_array)}',
                  f'DGP was {gf.dgpchoice(edges)}',
                  f'Penalty (from 0 to 10) is equal to {gf.fine(gf.userschoice(store_array), gf.dgpchoice(edges))}',
                  f"User's accuracy (from 0 to 1) for the round is {accuracy}",
                  f"User's score (from 0 to 1) for the round is {round(player.score, 5)}",
                  f'The seed is {seed}',
                  ],
            accuracy=accuracy
        )

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


class Questionnaire(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == min(len(C.task_sequence), C.NUM_ROUNDS)

    form_model = 'player'
    form_fields = ['Aot_' + str(x + 1) for x in range(3)] + ['feedback']


class Questionnaire2(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == min(len(C.task_sequence), C.NUM_ROUNDS)

    form_model = 'player'
    form_fields = ['Aot_' + str(x + 1) for x in range(3)] + ['feedback']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):

    @staticmethod
    def payoff_func(player):
        data = [(0, 0, 0)] * C.NUM_ROUNDS
        sumaccuracy = 0
        sumscore = 0
        number_of_rounds = C.NUM_ROUNDS
        number_of_rounds = C.NUM_ROUNDS
        for i in range(number_of_rounds):
            data[i] = (i + 1, player.in_round(i + 1).accuracy, player.in_round(i + 1).score)
            sumaccuracy += player.in_round(i + 1).accuracy * C.Round_payoff
            sumscore += player.in_round(i + 1).score * C.Bonus
        player.participant.payoff = sumaccuracy + sumscore

    @staticmethod
    def is_displayed(player):
        return player.round_number == min(len(C.task_sequence), C.NUM_ROUNDS)

    @staticmethod
    def vars_for_template(player):
        data = [(0, 0, 0)] * C.NUM_ROUNDS
        sumaccuracy = 0
        sumscore = 0
        number_of_rounds = C.NUM_ROUNDS
        for i in range(number_of_rounds):
            data[i] = (i + 1, player.in_round(i + 1).accuracy, player.in_round(i + 1).score)
            sumaccuracy += player.in_round(i + 1).accuracy
            sumscore += player.in_round(i + 1).score

        mean_accuracy = round((sumaccuracy / number_of_rounds), 5)
        return dict(
            ekey=[
                f"player's score in the first round {player.in_round(1).score}",
                f"player's score in the second round {player.in_round(2).score}",
            ],
            number_of_rounds=number_of_rounds,
            data=data,
            mean_accuracy=mean_accuracy,
            total_score=sumscore
        )


if C.training:
    page_sequence = [Instruction, Training, DiagramTask, DiagramTest, Results]
else:
    page_sequence = [Instruction, DiagramTask, DiagramTest, Results]
