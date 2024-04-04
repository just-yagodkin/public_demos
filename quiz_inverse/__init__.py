from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz_inverse'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_1 = models.StringField(
        choices=["The Y in this line is affected by another strong immature Z=0",
                 "The Y in this line is affected by another strong immature Z=1",
                 "The row/flower bed is on rocky soil",
                 "The value on a separate flower bed may appear accidentally",
                 "The row/flower bed is on sandy soil"],
        label='1.   If X is strong and mature and Y is weak and immature, note all conditions under which values of X=1 and Y=0 can be observed',
        widget=widgets.RadioSelect)

    q_2 = models.StringField(
        choices=["12",
                 "16",
                 "8"],
        label='2.   How many of the beds can be on rocky soil?',
        widget=widgets.RadioSelect)

    q_3 = models.StringField(
        choices=['X=1 can change the state of immature Y, initially equal to 0, to Y=1 in the first flowerbed/row',
                 'X=0 can change the state of mature Y, initially equal to 1, to Y=0 in the first flowerbed/row',
                 'X=1 can, in the first flowerbed/row, change the state of immature Y, initially equal to 0, to Y=1, and at the same time, X=1 can, in the second flowerbed/row, change the state of mature Y, initially equal to 1, to Y=0',
                 'X=1 can change the state of mature Y, initially equal to 1, to Y=0 in the first flowerbed/row',
                 'X=0 can in the first flowerbed/row change the state of immature Y, initially equal to 1, to Y=1'],
        label='3.   Select the incorrect ending(s) for the statement. If the first and second flower bed are on sandy soil (strong and weak influences work), then if X is strong and Y is weak',
        widget=widgets.RadioSelect)

    q_4 = models.StringField(
        choices=["It is immature (a property of Y itself).",
                 "It is weak (Influence of another strong immature Seed)",
                 "It is immature and/or weak"],
        label='4.   Name all possible reasons why seed Y did not germinate',
        widget=widgets.RadioSelect)

    q_5 = models.StringField(
        choices=['X is weak and Y is strong',
                 'X is strong and Y is weak',
                 'X is neither strong nor weak Y is neither strong nor weak'],
        label='5.   Consider a simplified problem where observations of only 2 seed varieties are demonstrated, located only over sandy soils, and all mature seeds are known and marked in orange (watch Table 1 below). Then the following types of dependence between seeds X and Y can be excluded:',
        widget=widgets.RadioSelect)

    q_6 = models.StringField(
        choices=["Z->Y, Y->X, X->Y",
                 "Z->Y, X->Y, X->Z",
                 "X->Y, X->Z, Y->X"],
        label='6.   If you already know that Y is strong in relation to Z, and Z is strong in relation to X, select the item that lists all the connections between strong and weak seeds that cannot exist:',
        widget=widgets.RadioSelect)

    q_7 = models.StringField(
        choices=["will germinate if it is mature",
                 "will germinate if it is not on rocky soil",
                 "will not germinate if it is on sandy soil"],
        label='7.   Complete the phrase correctly: neutral (neither strong nor weak) seed...',
        widget=widgets.RadioSelect)

    q_8 = models.StringField(
        choices=["rocky soils are found in flower beds with the same numbers",
                 "the number of strong and weak bonds is the same, but different types of seeds may be strong or weak compared to the original planet",
                 "the same number of mature seeds are planted on rocky soils as on the original planet"],
        label='8.   Complete the phrase correctly: on a twin planet...',
        widget=widgets.RadioSelect)


# PAGES

class Instruction(Page):
    pass

class Quiz(Page):

    form_model = 'player'
    form_fields = ['q_1', 'q_2', 'q_3', 'q_4', 'q_5', 'q_6', 'q_7', 'q_8']

    @staticmethod
    def error_message(player, values):
        #print('values is', values)
        if (values['q_1'] != "The Y in this line is affected by another strong immature Z=0" or
            values['q_2'] != "8" or
            values['q_3'] != 'X=1 can, in the first flowerbed/row, change the state of immature Y, initially equal to 0, to Y=1, and at the same time, X=1 can, in the second flowerbed/row, change the state of mature Y, initially equal to 1, to Y=0' or
            values['q_4'] != "It is immature and/or weak" or
            values['q_5'] != 'X is weak and Y is strong' or
            values['q_6'] != "Z->Y, X->Y, X->Z" or
            values['q_7'] != "will germinate if it is mature" or
            values['q_8'] != "the same number of mature seeds are planted on rocky soils as on the original planet"
        ):
            return 'В ответах есть ошибка'



class MyPage1(Page):
    #form_model = 'player'
    #form_fields = ['Aot_' + str(x + 1) for x in range(7)] + ['Age']
    pass



page_sequence = [Instruction, Quiz]
