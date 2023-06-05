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
    Aot_1 = models.StringField(
        choices=["Не помню/Не писал", "0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90",
                 "91-100"],
        label='Укажите какой у Вас был балл ЕГЭ по математике',
        widget=widgets.RadioSelectHorizontal)

    Aot_2 = models.StringField(
        choices=["Муж.", "Жен."],
        label='Выберите пол участника',
        widget=widgets.RadioSelectHorizontal)

    Aot_3 = models.IntegerField(
        min=1, max=10,
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Голодны ли Вы сейчас? 1-совсем не голоден(-на); 10-очень голоден(-на)',
        widget=widgets.RadioSelectHorizontal)

    Aot_4 = models.StringField(
        choices=["8-10", "10-12", "12-14", "14-16", "16-18", "18-20", "20-22"],
        label='Укажите время суток эксперимента',
        widget=widgets.RadioSelectHorizontal)

    Aot_5 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Оцените Ваш сегодняшний сон. 1-плохо спал(-а); 10-хорошо спал(-а)',
        widget=widgets.RadioSelectHorizontal)

    Aot_6 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Оцените Ваш уровень усталости. 1-очень устал(-а); 10-совсем не устал(-а)',
        widget=widgets.RadioSelectHorizontal)

    Aot_7 = models.StringField(
        choices=["Ничего из этого не было", "Был только один курс", "Было только два курса", "Все курсы были"],
        label='Были ли у Вас курсы по теории вероятностей/статистики/высшей математики?',
        widget=widgets.RadioSelectHorizontal)

    Age = models.StringField(label="Укажите Ваш возраст")

    feedback1 = models.StringField(label="Общие пожелания и комментарии")

    feedback2 = models.StringField(label="Были ли понятны инструкции? Если нет, то что было непонятно?")

    feedback3 = models.StringField(label="Какова была Ваша стратегия при выборе ответов?")

    feedback4 = models.StringField(label="Было ли понятно, что нас интересуют причинно-следственные связи?")
    #
    # Aot_5 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Менять свое мнение — признак слабости.',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_6 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Людям следует активно искать причины, по которым они могут оказаться неправы.',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_7 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Можно не учитывать свидетельства против убеждений, в которых уверен(а).',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_8 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Важно придерживаться своих убеждений, даже когда предоставлены свидетельства, говорящие об обратном.',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_9 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Правильное мышление, в случае если есть хорошие аргументы за обе стороны, приводит к нерешительности.',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_10 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Прежде чем принимать решение по поводу сложного вопроса, нужно рассмотреть больше одного возможного варианта ответа.',
    #     widget=widgets.RadioSelectHorizontal)
    #
    # Aot_11 = models.IntegerField(
    #     min=1, max=5,
    #     choices=[0, 1, 2, 3, 4, 5],
    #     label='Лучше быть уверенным в умозаключении даже если есть веские причины сомневаться в нем.',
    #     widget=widgets.RadioSelectHorizontal)


# PAGES
class MyPage1(Page):
    form_model = 'player'
    form_fields = ['Aot_' + str(x + 1) for x in range(7)] + ['Age']

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['feedback' + str(x + 1) for x in range(4)]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage1, MyPage2]
