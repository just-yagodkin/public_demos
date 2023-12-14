from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quizeng'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_1 = models.StringField(
        choices=["Семена не растут.", "Не растут незрелые и слабые незрелые семена.",
                 "Не растут только слабые семена."],
        label='1.   На каменистых почвах',
        widget=widgets.RadioSelectHorizontal)

    q_2 = models.StringField(
        choices=["12", "16", "8"],
        label='2.   Сколько из 16 клумб могут быть на каменистой почве?',
        widget=widgets.RadioSelectHorizontal)

    q_3 = models.StringField(
        choices=['Оно незрелое', 'Оно слабое', 'Оно не зрелое и/или слабое'],
        label='3.   Назовите все возможные причины того, что семя не проросло.',
        widget=widgets.RadioSelectHorizontal)

    q_4 = models.StringField(
        choices=["X слабое и Y сильное.", "X сильное и Y слабое.", "X не сильное и не слабое Y сильное.",
                 "X не сильное и не слабое Y не сильное и не слабое."],
        label='4.   Рассмотрим упрощённую задачу (см. Таблицу 1), где продемонстрированы наблюдения только 2-х типов семян, расположенных только над песчаными почвами, и все зрелые семена известны и помечены оранжевым цветом. Тогда зависимости между типами семян будут:',
        widget=widgets.RadioSelectHorizontal)

    q_5 = models.StringField(
        choices=['Семя Y на клумбе 7 проросло на планете близнеце (справа), потому что оно сильное.',
                 'Семя Y на клумбе 7 не проросло на планете (слева), потому что оно слабое.',
                 'Семя Y на клумбе 3 не проросло, потому что оно на каменистой почве, оно слабое и незрелое.'],
        label='5.   Рассмотрим теперь, точно такие же наблюдения (см. Таблицу 2), но два отличия приближают их обратно к не упрощённому заданию. Первое: зрелые семена так же расположены по тем же номерам клумб, но больше нет выделения цветом. Второе: клумба №1 в таблице слева и клумба №3 в таблице справа теперь находятся на каменистых почвах. Обратите внимание, что хоть номера клумб и не совпадают, количество зрелых семян, распределённое по каменистым клумбам всегда одинаковое на обоих планетах. Выберете правильное утверждение:',
        widget=widgets.RadioSelectHorizontal)

    q_6 = models.StringField(
        choices=['Z->Y, Y->X, X->Y', 'Z->Y, X->Y, X->Z', 'X->Y, X->Z, Y->X'],
        label='6.   Если уже известно, что Y сильное по отношению к Z, а Z cильное по отношению к X выберете пункт, в котором перечислены вся связи между сильными и слабыми семенами, которых не может быть:',
        widget=widgets.RadioSelectHorizontal)

    q_7 = models.StringField(
        choices=["Прорастёт если оно зрелое.", "Прорастёт если оно не на каменистой почве.",
                 "Не прорастёт если оно на песчаной почве."],
        label='7.   Завершите фразу корректно: нейтральное (не сильное и не слабое) семя:',
        widget=widgets.RadioSelectHorizontal)

    q_8 = models.StringField(
        choices=["Каменистые почвы находятся в клумбах с такими же номерами.",
                 "Количество сильных и слабых связей одинаково, но разные типы семян могут быть сильными или слабыми в сравнении с оригинальной планетой.",
                 "То же количество зрелых семян посажено на каменистых почвах, что и на планете-оригинале."],
        label='8.   Завершите фразу корректно: на планете двойнике',
        widget=widgets.RadioSelectHorizontal)


# PAGES

class Instruction(Page):
    pass

class Quiz(Page):

    form_model = 'player'
    form_fields = ['q_1', 'q_2', 'q_3', 'q_4', 'q_5', 'q_6', 'q_7', 'q_8']

    @staticmethod
    def error_message(player, values):
        #print('values is', values)
        if (values['q_1'] != "Не растут незрелые и слабые незрелые семена." or
            values['q_2'] != "8" or
            values['q_3'] != 'Оно не зрелое и/или слабое' or
            values['q_4'] != "X сильное и Y слабое." or
            values['q_5'] != 'Семя Y на клумбе 3 не проросло, потому что оно на каменистой почве, оно слабое и незрелое.' or
            values['q_6'] != 'Z->Y, X->Y, X->Z' or
            values['q_7'] != "Прорастёт если оно зрелое." or
            values['q_8'] != "То же количество зрелых семян посажено на каменистых почвах, что и на планете-оригинале."
        ):
            return 'В ответах есть ошибка'



class MyPage1(Page):
    #form_model = 'player'
    #form_fields = ['Aot_' + str(x + 1) for x in range(7)] + ['Age']
    pass



page_sequence = [Instruction, Quiz]
