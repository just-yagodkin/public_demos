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
    Round_payoff = 1
    NUM_ROUNDS = 18
    SHOWING_INFORMATION_EDGE = 0.0  # you will see a feedback only after this percent of rounds
    NAME_IN_URL = 'data_to_dgp_new'
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

    # task_sequence = ["twolinks", "collider1", "threelinks", "twolinks", "fork", "nolinks", "onelink"]
    task_sequence = basis1 + basis2 + basis3

    seed = [(name, random.randint(0, 5)) for name in task_sequence]

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

    # silver = old control
    preinterventional_data_silver = [[x[0], gf.smartdatainterv(gf.color_intervente(x[0], gf.original_data[x[0]], 's'), x[1])] for x in seed]
    preinterventional_data_yellow = [[x[0], gf.smartdatainterv(gf.color_intervente(x[0], gf.original_data[x[0]], 'y'), x[1])] for x in seed]
    preinterventional_data_green = [[x[0], gf.smartdatainterv(gf.color_intervente(x[0], gf.original_data[x[0]], 'g'), x[1])] for x in seed]


    if len(task_sequence) < NUM_ROUNDS:
        NUM_ROUNDS = len(task_sequence)

    edge = NUM_ROUNDS * SHOWING_INFORMATION_EDGE

    observational_data = gf.reshuffle(preobservational_data)
    interventional_data_silver = gf.reshuffle(preinterventional_data_silver)
    interventional_data_yellow = gf.reshuffle(preinterventional_data_yellow)
    interventional_data_green = gf.reshuffle(preinterventional_data_green)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dgptype = models.StringField(initial="")
    userdgp = models.StringField(initial="")
    userdgp_exclude = models.StringField(initial="")
    backtransform_userdgp_exclude = models.StringField(initial="")
    originaldgp = models.StringField(initial="")

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

    radio_buttons = models.StringField(initial='[0,0,0,0,0,0,0,0,0]')
    backtransform_radio_buttons = models.StringField(initial='[0,0,0,0,0,0,0,0,0]')
    right_answers = models.StringField(initial='[0,0,0,0,0,0,0,0,0]')
    right_answers_after_seed = models.StringField(initial='[0,0,0,0,0,0,0,0,0]')

    penalty = models.IntegerField(initial=0)
    accuracy = models.IntegerField(initial=0)
    score = models.FloatField(initial=0)

    treatment = models.StringField()
    node = models.StringField(initial='')
    backtransform_node = models.StringField(initial='')
    seed = models.IntegerField(initial=0)
    round_num = models.IntegerField(initial=0)

    payoff_for_score = models.FloatField(initial=0)
    payoff_for_accuracy = models.FloatField(initial=0)

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
    # 'g' is for green, 'y' is for yellow, 's' is for silver
    possible_treatments = ('gys', 'gsy', 'ysg', 'ygs', 'syg', 'sgy')

    if C.treatment:
        treatments = itertools.cycle(possible_treatments)
        for player in subsession.get_players():
            player.treatment = next(treatments)


# Functions
def datatask_output_json(player: Player):
    num_round = player.round_number - 1
    if num_round <= 5:
        if player.treatment[0] == 's':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_silver[num_round][1]]
        if player.treatment[0] == 'y':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_yellow[num_round][1]]
        if player.treatment[0] == 'g':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_green[num_round][1]]

    if 5 < num_round <= 11:
        if player.treatment[1] == 's':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_silver[num_round][1]]
        if player.treatment[1] == 'y':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_yellow[num_round][1]]
        if player.treatment[1] == 'g':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_green[num_round][1]]

    if 11 < num_round <= 17:
        if player.treatment[2] == 's':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_silver[num_round][1]]
        if player.treatment[2] == 'y':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_yellow[num_round][1]]
        if player.treatment[2] == 'g':
            target_vocabulary = [C.observational_data[num_round][1], C.interventional_data_green[num_round][1]]

    return target_vocabulary


def benchmark_diagram(player: Player):
    num_round = player.round_number - 1
    # target_key = C.task_sequence[num_round]
    target_vocabulary = C.data_edges[num_round]

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
    form_fields = ['conf_init', 'stored', 'conf_bid', 'buttons', 'radio_buttons']

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
            buttons=values['buttons'],
            radio_buttons=values['radio_buttons']
        )

        # Converting string to list
        res = json.loads(values['buttons']).copy()
        # print(res)

        player.round_num = player.round_number

        if values['conf_init'] != values['conf_bid']:
            player.conf_bid_is_random = 0

        player.stored_check = player.stored

        player.originaldgp = json.dumps(gf.dgpchoice(benchmark_diagram(player)))

        player.userdgp = json.dumps(gf.userschoice(player.stored))
        player.dgptype = C.task_sequence[player.round_number - 1]

        player.seed = C.seed[player.round_number - 1][1]

        if gf.take_color(player.treatment, player.round_number - 1) == 's':
            player.node = gf.wherey(C.seed[player.round_number - 1][1])
            player.backtransform_node = 'Y'
        elif gf.take_color(player.treatment, player.round_number - 1) == 'y':
            player.node = gf.wherex(C.seed[player.round_number - 1][1])
            player.backtransform_node = 'X'
        elif gf.take_color(player.treatment, player.round_number - 1) == 'g' and player.dgptype in ['onelink', 'twolinks', 'threelinks']:
            player.node = gf.wherez(C.seed[player.round_number - 1][1])
            player.backtransform_node = 'Z'
        else:
            player.node = 'N'
            player.backtransform_node = 'N'


        player.edges_num = len(json.loads(player.originaldgp))

        error_messages = dict()

        player.right_answers = str(gf.right_answers(player.dgptype, gf.take_color(player.treatment, player.round_number-1)))

        right_answers_after_seed = gf.right_answers_after_seed(json.loads(player.right_answers), player.seed)
        player.right_answers_after_seed = json.dumps(right_answers_after_seed)

        # radio_buttons = json.loads(player.radio_buttons)
        radio_buttons = json.loads(solutions['radio_buttons'])

        player.backtransform_radio_buttons = json.dumps(gf.user_radio_buttons_before_seed(radio_buttons, player.seed))
        penalty = sum([abs(x - y) for x, y in zip(right_answers_after_seed, radio_buttons)])
        player.penalty = penalty

        accuracy = 9 - penalty
        player.accuracy = accuracy

        print(accuracy)

        temp = ['XY', 'YX', 'NXY', 'XZ', 'ZX', 'NXZ', 'YZ', 'ZY', 'NYZ']
        userdgp_exclude = []
        for i in range(len(radio_buttons)):
            if radio_buttons[i] == 1:
                userdgp_exclude.append(temp[i])

        player.userdgp_exclude = json.dumps(userdgp_exclude)

        player.backtransform_userdgp_exclude = gf.transfom_userdgp(s=player.userdgp_exclude,
                                                                   seed=C.seed[player.round_number - 1][1])

        # предлагаю кстати отказаться от ^2
        # player.score = 1 - round((values['conf_bid'] * 0.01 - (9 - player.accuracy) ** 2 / 9), 5)  # score от 0 до 1

        # score от 0 до 1
        score = 1 - abs(values['conf_bid'] * 0.01 - player.accuracy/9)
        player.score = round(score, 4)

        player.payoff_for_score = round(score * C.Bonus, 2)
        player.payoff_for_accuracy = accuracy * C.Round_payoff
        player.payoff = cu(player.payoff_for_score + player.payoff_for_accuracy)

        return error_messages

    @staticmethod
    def vars_for_template(player):
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
            treatment=player.treatment,
            seed=C.seed[player.round_number - 1][1],
            dgptype=C.task_sequence[player.round_number - 1],
            round_number=player.round_number
        )

    @staticmethod
    def js_vars(player):
        output = datatask_output_json(player)
        datasetobs = [(i + 1, output[0]['x'][i], output[0]['y'][i], output[0]['z'][i]) for i in range(16)]
        datasetint = [(i + 1, output[1]['x'][i], output[1]['y'][i], output[1]['z'][i]) for i in range(16)]
        dgptype = C.task_sequence[player.round_number - 1]
        color = gf.take_color(player.treatment, player.round_number-1)

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
            dgptype=dgptype,
            color=color,
            forcebutton=gf.has_do(dgptype, color)
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
            datasetint = C.interventional_data_silver[player.round_number - 1][1]
        else:
            datasetint = C.interventional_data_treatment[player.round_number - 1][1]

        buttons_were_clicked = json.loads(player.buttons)

        accuracy = player.accuracy

        return dict(
            ekey=[f'The original sequence is {C.task_sequence}',
                  f'User did not set cycles: {gf.tanc(store_array)}',
                  f'User chose {gf.userschoice(store_array)}',
                  f'DGP was {gf.dgpchoice(edges)}',
                  f"User's accuracy (from 0 to 9) for the round is {accuracy}",
                  f"User's score (from 0 to 1) for the round is {round(player.score, 4)}",
                  f'The seed is {seed}',
                  f'Treatment = {treatment}'
                  f'Node is {player.node}'
                  ],
            accuracy=accuracy,
            payoff_for_score=player.payoff_for_score,
            payoff_for_accuracy=player.payoff_for_accuracy
        )

    @staticmethod
    def js_vars(player):
        benchmark_edges = benchmark_diagram(player)

        right_answers_list = json.loads(player.right_answers_after_seed)
        player_answers = json.loads(player.radio_buttons)

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
            show_edges_template=show_edges,
            right_answers_list=right_answers_list,
            player_answers=player_answers,
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
