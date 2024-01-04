from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz_eng'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_1 = models.StringField(
        choices=["Seeds do not grow", "Immature and weak immature seeds do not grow",
                 "Only weak seeds don't grow"],
        label='1.   On the rocky soils',
        widget=widgets.RadioSelectHorizontal)

    q_2 = models.StringField(
        choices=["12", "16", "8"],
        label='2.   How many of the beds can be on rocky soil?',
        widget=widgets.RadioSelectHorizontal)

    q_3 = models.StringField(
        choices=['It is immature', 'It is weak', 'It is immature or/and it is weak'],
        label='3.  List all the possible explanations  why the seed did not germinate',
        widget=widgets.RadioSelectHorizontal)

    q_4 = models.StringField(
        choices=["X is weak and Y is strong", "X is strong and Y is weak", "X is neither strong nor weak Y is strong",
                 "X is neither strong nor weak Y is neither strong nor weak."],
        label='4.  Consider a simplified problem (see Table 1) where observations of only 2 seed types are demonstrated, located only over sandy soils, and all mature seeds are known and labeled orange. Then the dependencies between seed types will be:',
        widget=widgets.RadioSelectHorizontal)

    q_5 = models.StringField(
    choices=['Seed Y in flowerbed 7 has germinated on the twin planet (right) because it is strong.',
                 'Seed Y on bed 7 did not germinate on planet (left) because it is weak.',
                 'Seed Y on bed 3 did not germinate because it is on stony soil, it is weak and immature.'],
        label='5.   Consider now, exactly the same observations (see Table 2), but two differences bring them back closer to the unsimplified assignment. The first: the mature seeds are similarly arranged by the same bed numbers, but there is no longer any highlighting by colour. Two: bed number 1 in the table on the left and bed number 3 in the table on the right are now on rocky soils. Note that although the bed numbers are not the same, the number of mature seeds distributed on the rocky beds is always the same on both planets. Choose the correct statement:',
          widget=widgets.RadioSelectHorizontal)

    q_6 = models.StringField(
        choices=['Z->Y, Y->X, X->Y', 'Z->Y, X->Y, X->Z', 'X->Y, X->Z, Y->X'],
        label='6. If it is already known that Y is strong with respect to Z and Z is strong with respect to X choose the item that lists all the relationships between strong and weak seeds that cannot be:',
        widget=widgets.RadioSelectHorizontal)

    q_7 = models.StringField(
        choices=["Will germinate if it's mature", "Will germinate if it's not on rocky soil",
                 "Will not germinate if it's on sandy soil"],
        label='7.   Complete the sentence correctly: neutral (neither strong nor weak) seed:',
        widget=widgets.RadioSelectHorizontal)

    q_8 = models.StringField(
        choices=["Rocky soils are found in beds with the same numbers.",
                 "The number of strong and weak links are the same, but different types of seeds may be strong or weak compared to the original planet.",
                 "The same number of mature seeds are planted on rocky soils as on the original planet."],
        label='8.   Complete the sentence correctly: on the twin planet',
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
        if (values['q_1'] != "Immature and weak immature seeds do not grow" or
            values['q_2'] != "8" or
            values['q_3'] != 'It is immature or/and it is weak' or
            values['q_4'] != "X is strong and Y is weak" or
            values['q_5'] != 'Seed Y on bed 3 did not germinate because it is on stony soil, it is weak and immature.' or
            values['q_6'] != 'Z->Y, X->Y, X->Z' or
            values['q_7'] != "Will germinate if it's mature" or
            values['q_8'] != "The same number of mature seeds are planted on rocky soils as on the original planet."
        ):
            return 'the responses contain a mistake(s)'



class MyPage1(Page):
    #form_model = 'player'
    #form_fields = ['Aot_' + str(x + 1) for x in range(7)] + ['Age']
    pass



page_sequence = [Instruction, Quiz]
