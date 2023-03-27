from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'AOT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Aot_1 = models.IntegerField(
        min=1, max=5,
        choices = [0,1,2,3,4,5],
        label='Настоящие эксперты готовы признаться себе и другим, что они не уверены или не знают ответа.',
        widget=widgets.RadioSelectHorizontal)
    
    Aot_2 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Людям следует принимать во внимание свидетельства, противоречащие их позиции.',
    widget=widgets.RadioSelectHorizontal)

    Aot_3 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Нерешительность или неуверенность — следствие запутанных мыслей.',
    widget=widgets.RadioSelectHorizontal)

    Aot_4 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Людям следует пересматривать свою позицию в связи с появлением новой актуальной информации.',
    widget=widgets.RadioSelectHorizontal)

    Aot_5 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Менять свое мнение — признак слабости.',
    widget=widgets.RadioSelectHorizontal)

    Aot_6 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Людям следует активно искать причины, по которым они могут оказаться неправы.',
    widget=widgets.RadioSelectHorizontal)


    Aot_7 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Можно не учитывать свидетельства против убеждений, в которых уверен(а).',
    widget=widgets.RadioSelectHorizontal)


    Aot_8 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Важно придерживаться своих убеждений, даже когда предоставлены свидетельства, говорящие об обратном.',
    widget=widgets.RadioSelectHorizontal)


    Aot_9 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Правильное мышление, в случае если есть хорошие аргументы за обе стороны, приводит к нерешительности.',
    widget=widgets.RadioSelectHorizontal)


    Aot_10 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Прежде чем принимать решение по поводу сложного вопроса, нужно рассмотреть больше одного возможного варианта ответа.',
    widget=widgets.RadioSelectHorizontal)


    Aot_11 = models.IntegerField(
    min=1, max=5,
    choices = [0,1,2,3,4,5],
    label='Лучше быть уверенным в умозаключении даже если есть веские причины сомневаться в нем.',
    widget=widgets.RadioSelectHorizontal)



# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['Aot_' + str(x+1) for x in range(11)]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
