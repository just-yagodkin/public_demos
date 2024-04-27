import copy

from otree.api import *
import goodfunctions as gf
import random
import json
import itertools

doc = """
Your app description
"""


class C(BaseConstants):
    train = False
    treatment = True
    Bonus = 5
    Round_payoff = 10
    NUM_ROUNDS = 18
    SHOWING_INFORMATION_EDGE = 0.0  # you will see a feedback only after this percent of rounds

    NAME_IN_URL = 'data_to_dgp'
    PLAYERS_PER_GROUP = None

    conf_range = range(101)

    basis1 = ["nolinks", "onelink", "twolinks", "collider1", "fork", "threelinks"]
    basis2 = ["nolinks", "onelink", "twolinks", "collider1", "fork", "threelinks"]
    basis3 = ["nolinks", "onelink", "twolinks", "collider1", "fork", "threelinks"]
    random.shuffle(basis1)
    random.shuffle(basis2)
    random.shuffle(basis3)

    while basis2[0] == basis1[5] or basis2[5] == basis3[0]:
        random.shuffle(basis2)

    # task_sequence = ["onelink", "twolinks", "collider1", "threelinks", "twolinks", "fork", "nolinks", "onelink"]
    task_sequence = basis1 + basis2 + basis3

    seed = [(name, random.randint(0, 5)) for name in task_sequence]
    # если надо зафиксировать сид, то надо раскоментить строочку ниже
    # seed = [(name, 0) for name in task_sequence]

    pretraining = {'left': {'x': [1, 1, 1, 1, 0, 0, 0, 0], 'y': [1, 1, 1, 1, 1, 1, 0, 0]},
                   'right': {'x': [1, 1, 1, 1, 1, 1, 1, 1], 'y': [1, 1, 1, 1, 1, 1, 1, 1]}}

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

    data_edges = []
    for i in range(len(seed)):
        data_edges.append(gf.smartedgesinterv(pre_data_edges[seed[i][0]], seed[i][1]))

    original_data = {'nolinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                                 'z': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]},
                     'onelink': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 'y': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                 'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
                     'twolinks': {'x': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  'z': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
                     'collider1': {'x': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                                   'y': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                                   'z': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
                     'fork': {'x': [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              'y': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              'z': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                     'threelinks': {'x': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'y': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                    'z': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
                     }

    pre_preobservational_data = copy.deepcopy(original_data)

    preobservational_data = [[x[0], gf.smartdatainterv(gf.pre_preobservational_data[x[0]], x[1])] for x in seed]

    preinterventional_data = [[x[0], gf.smartdatainterv(gf.intervente(x[0], gf.original_data[x[0]]), x[1])] for x in
                              seed]

    # X -> Y ->
    # |       |
    # |       V
    # ▶  ->  Z

    preinterventional_data_treatment = [
        [x[0], gf.smartdatainterv(gf.intervente(x[0], gf.original_data[x[0]]), x[1])] if (
                x[0] not in ['onelink', 'twolinks', 'collider1']) else [x[0], gf.smartdatainterv(
            gf.intervente(x[0], gf.original_data[x[0]], name='x'), x[1])] for x in seed]


    if len(task_sequence) < NUM_ROUNDS:
        NUM_ROUNDS = len(task_sequence)

    edge = NUM_ROUNDS * SHOWING_INFORMATION_EDGE

    observational_data = gf.reshuffle(preobservational_data)
    interventional_data = gf.reshuffle(preinterventional_data)
    interventional_data_treatment = gf.reshuffle(preinterventional_data_treatment)

    # если надо, чтобы строки не шафлились раскоментируйте 3 строчки ниже
    # observational_data = preobservational_data
    # interventional_data = preinterventional_data
    # interventional_data_treatment = preinterventional_data_treatment

    # print(observational_data)
    # print()
    # print(interventional_data_treatment)
    # print()
    # print(interventional_data)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dgptype = models.StringField(initial="")

    userdgp = models.StringField(initial="")
    backtransform_userdgp = models.StringField(initial="")

    originaldgp = models.StringField(initial="")

    dir_error = models.IntegerField(initial=0)
    struct_error = models.IntegerField(initial=0)
    error_counter = models.IntegerField(initial=0)
    edges_num = models.IntegerField()

    stored = models.StringField(initial=json.dumps(
        [{"data": {"counter": 0, "id": "X", "name": "X"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Y", "name": "Y"}, "style": {"background-color": "#c3cec0"}},
         {"data": {"counter": 0, "id": "Z", "name": "Z"}, "style": {"background-color": "#c3cec0"}}]))

    stored_check = models.StringField(initial=0)

    training = models.BooleanField()

    conf_init = models.IntegerField()

    conf_bid = models.IntegerField(initial=-1,
                                   choices=[i for i in C.conf_range],
                                   # widget=widgets.RadioSelect,
                                   )

    conf_bid_is_random = models.IntegerField(initial=1)

    buttons = models.StringField()

    buttons_before_err = models.StringField(initial='[0,0,0,0,0,0,0,0,0,0,0,0,0,0]')

    score = models.FloatField(initial=0)

    accuracy = models.FloatField()

    err_counter = models.IntegerField(initial=0)  # ошибок всего

    cycle_err = models.IntegerField(initial=0)  # есть ли ошибка цикла прямо здесь и сейчас

    treatment = models.BooleanField()

    node = models.StringField(initial='')
    backtransform_node = models.StringField(initial='')

    seed = models.IntegerField(initial=0)

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


def creating_session(subsession):
    if C.treatment:
        treatments = itertools.cycle([False, True, True])
        for player in subsession.get_players():
            player.treatment = next(treatments)


# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number - 1
    target_key = C.task_sequence[num_round]
    if player.treatment:
        target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_treatment[num_round][1]]
    else:
        target_vocabulary = [C.observational_data[num_round][1], C.interventional_data[num_round][1]]

    # print(target_vocabulary)
    # print('Я ТУТ!!!!!!!!!!!!!')

    return target_vocabulary


def benchmark_diagram(player: Player):
    num_round = player.round_number - 1
    # target_key = C.task_sequence[num_round]
    target_vocabulary = C.data_edges[num_round]
    # print(C.data_edges)
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
    # print(C.improved_task_sequence)
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

        player.training = (newdata == [1, 0, 0, 0, 0, 0])  ###  TRUE if X -> Y
        return {1: player.training}

    def error_message(player, values):
        solutions = dict(
            training=True,
        )
        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Форма заполнена неверно'
        return error_messages


class Training2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        left = C.pretraining['left']
        right = C.pretraining['right']

        return dict(
            datasetobs=[(i + 1, left['x'][i], left['y'][i]) for i in range(len(left['x']))],
            datasetint=[(i + 1, right['x'][i], right['y'][i]) for i in range(len(right['x']))],
            frequenciesobs=["freq"] + ['0.5'] + ['0.75'],
            frequenciesint=["freq"] + ['1'] + ['1']
        )


class DiagramTask(Page):
    form_model = 'player'
    form_fields = ['conf_init', 'stored', 'conf_bid', 'buttons']

    @staticmethod
    def live_method(player, data):
        player.stored = json.dumps(data)
        # print(player.stored)

        return {1: player.stored}

    def error_message(player, values):

        print(values)

        values['stored'] = gf.tanc(player.stored)
        solutions = dict(
            conf_init=values['conf_init'],
            stored=True,
            conf_bid=values['conf_bid'],
            buttons=values['buttons']
        )

        # print(solutions)
        if values['stored'] != solutions['stored']:
            player.cycle_err = 1
        else:
            player.cycle_err = 0

        # Converting string to list
        res = json.loads(values['buttons']).copy()
        res_before_errors = json.loads(player.buttons_before_err).copy()

        for i in range(12):  # 12 = num of buttons
            res[i] += res_before_errors[i]

        # print(res)

        if values['conf_init'] != values['conf_bid']:
            player.conf_bid_is_random = 0

        player.stored_check = player.stored
        player.accuracy = round(
            gf.accuracy(gf.fine(gf.userschoice(player.stored), gf.dgpchoice(benchmark_diagram(player)))), 12)
        player.score = 1 - round((values['conf_bid'] * 0.01 - player.accuracy) ** 2, 5)

        player.originaldgp = json.dumps(gf.dgpchoice(benchmark_diagram(player)))

        player.userdgp = json.dumps(gf.userschoice(player.stored))
        player.backtransform_userdgp = gf.transfom_userdgp(s=player.userdgp,
                                                           seed=C.seed[player.round_number - 1][1])

        player.dgptype = C.task_sequence[player.round_number - 1]

        player.seed = C.seed[player.round_number - 1][1]

        if player.treatment and (player.dgptype in ['onelink', 'twolinks', 'collider1']):
            player.node = gf.wherex(C.seed[player.round_number - 1][1])
            player.backtransform_node = 'X'
        else:
            player.node = gf.wherey(C.seed[player.round_number - 1][1])
            player.backtransform_node = 'Y'

        player.dir_error = gf.directional_error(json.loads(player.userdgp), json.loads(player.originaldgp))
        player.struct_error = gf.structure_error(json.loads(player.userdgp), json.loads(player.originaldgp))
        player.error_counter = player.dir_error + player.struct_error
        player.edges_num = len(json.loads(player.originaldgp))

        error_messages = dict()

        if player.cycle_err == 1:
            error_messages['stored'] = 'В форме присутствует цикл'
            player.err_counter += 1
            player.stored = '[{"counter": 0, "weight": 0, "id": "XY", "source": "X", "target": "Y", "label": ""}, ' \
                            '{"counter": 0, "weight": 0, "id": "YX", "source": "Y", "target": "X", "label": ""}, ' \
                            '{"counter": 0, "weight": 0, "id": "YZ", "source": "Y", "target": "Z", "label": ""}, ' \
                            '{"counter": 0, "weight": 0, "id": "XZ", "source": "X", "target": "Z", "label": ""}, ' \
                            '{"counter": 0, "weight": 0, "id": "ZY", "source": "Z", "target": "Y", "label": ""}, ' \
                            '{"counter": 0, "weight": 0, "id": "ZX", "source": "Z", "target": "X", "label": ""}]'
            player.buttons_before_err = json.dumps(res)
            player.buttons = json.dumps([0] * 12)
            player.cycle_err = 0

        else:
            player.buttons = json.dumps(res)
            # print(json.dumps(res), "А ТУТ ВСЕ ПРАВИЛЬНО)")

        store_array = player.stored
        edges = benchmark_diagram(player)
        accuracy = round(gf.accuracy(gf.fine(gf.userschoice(store_array), gf.dgpchoice(edges))), 4)
        player.payoff = cu(round(player.score, 5) * C.Bonus + accuracy * C.Round_payoff)

        return error_messages

    @staticmethod
    def vars_for_template(player):
        output = datatask_output_json(player)

        datasetobs = [(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in range(16)]
        datasetint = [(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in range(16)]

        # choices = [(1, "X-сильное, Y-слабое"),
        #            (2, "Y-сильное, X-слабое"),
        #            (3, "X и Y нейтральные по отношению друг к другу"),
        #            (4, "Y-сильное, Z-слабое"),
        #            (5, "Z-сильное, Y-слабое"),
        #            (6, "Y и Z нейтральные по отношению друг к другу"),
        #            (7, "X-сильное, Z-слабое"),
        #            (8, "Z-сильное, X-слабое"),
        #            (9, "X и Z нейтральные по отношению друг к другу")]
        # print(datasetobs)

        return dict(
            datasetobs=datasetobs,
            datasetint=datasetint,
            frequenciesobs=["freq"] + [str(float('{:.2f}'.format(gf.check_frequencies(output[0])[0])))] + [
                str(float('{:.2f}'.format(gf.check_frequencies(output[0])[1])))] + [
                               str(float('{:.2f}'.format(gf.check_frequencies(output[0])[2])))],
            frequenciesint=["freq"] + [str(float('{:.2f}'.format(gf.check_frequencies(output[1])[0])))] + [
                str(float('{:.2f}'.format(gf.check_frequencies(output[1])[1])))] + [
                               str(float('{:.2f}'.format(gf.check_frequencies(output[1])[2])))],
            treatment=player.treatment,
            seed=C.seed[player.round_number - 1][1],
            dgptype=C.task_sequence[player.round_number - 1],
            # choices=choices
        )

    @staticmethod
    def js_vars(player):
        output = datatask_output_json(player)
        datasetobs = [(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in range(16)]
        datasetint = [(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in range(16)]

        return dict(
            datasetobs=datasetobs,
            datasetint=datasetint,
            frequenciesobs=["freq"] + [str(float('{:.2f}'.format(gf.check_frequencies(output[0])[0])))] + [
                str(float('{:.2f}'.format(gf.check_frequencies(output[0])[1])))] + [
                               str(float('{:.2f}'.format(gf.check_frequencies(output[0])[2])))],
            frequenciesint=["freq"] + [str(float('{:.2f}'.format(gf.check_frequencies(output[1])[0])))] + [
                str(float('{:.2f}'.format(gf.check_frequencies(output[1])[1])))] + [
                               str(float('{:.2f}'.format(gf.check_frequencies(output[1])[2])))],
            seed=C.seed[player.round_number - 1][1],
            treatment=player.treatment,
            dgptype=C.task_sequence[player.round_number - 1]
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
        treatment = player.treatment
        # print(edges)
        datasetobs = C.observational_data[player.round_number - 1][1]

        if treatment:
            datasetint = C.interventional_data[player.round_number - 1][1]
        else:
            datasetint = C.interventional_data_treatment[player.round_number - 1][1]

        buttons_were_clicked = json.loads(player.buttons)

        accuracy = player.accuracy
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
                  f'Treatment = {treatment}'
                  ],
            accuracy=accuracy
        )

    @staticmethod
    def js_vars(player):
        benchmark_edges = benchmark_diagram(player)

        store_array = json.loads(player.stored_check)
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


if C.train:
    page_sequence = [Instruction, Training, Training2, DiagramTask, DiagramTest, Results]
else:
    page_sequence = [DiagramTask, DiagramTest, Results]
