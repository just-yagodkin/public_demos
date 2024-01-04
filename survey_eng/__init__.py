from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey_eng'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Aot_1 = models.StringField(blank=True,   
        label='If you remember, indicate what your grade was in your school math final exam.')

    Aot_2 = models.StringField(
        choices=["Male.", "Female.", "Oth.", "Prefer not disclose"],
        label='Select the gender of the participant',
        widget=widgets.RadioSelectHorizontal)

    Aot_3 = models.IntegerField(
        min=1, max=10,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Are you hungry now? 1-not at all hungry; 10-very hungry',
        widget=widgets.RadioSelectHorizontal)

    Aot_4 = models.StringField(
        choices=["8-10am", "10-12am", "0-2pm", "2-4pm", "4-6pm", "6-8pm", "8-10pm"],
        label='Specify the time of day of the experiment',
        widget=widgets.RadioSelectHorizontal)

    Aot_5 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Rate sleep today from 1-didn nott sleep well to 10-good sleep.',
        widget=widgets.RadioSelectHorizontal)

    Aot_6 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Rate your level of tiredness. 1 - very tired; 10 - not tired at all',
        widget=widgets.RadioSelectHorizontal)

    Aot_7 = models.StringField(
        choices=["None of these were", "There was only one course", "There were only two courses", "All courses were"],
        label='Did you have any courses in probability theory/statistics/higher math?',
        widget=widgets.RadioSelectHorizontal)

    Age = models.IntegerField(
        min=14, max=90,
        label='Indicate the age of the participant')

    feedback1 = models.StringField(label="general suggestions and wishes")

    feedback2 = models.StringField(label="Were instructions clear?  If not, what was unclear? ")

    feedback3 = models.StringField(
        label=" Do you think there is a difference between the two tables (data from the original planet and the twin planet respectively), if so what is the difference?")

    feedback4 = models.StringField(label="What was your strategy in selecting your answers?")

    feedback5 = models.StringField(
        label=" Was it clear that the data from the twin planet was identical to the data that would have been obtained by conducting an experiment (transplanting some of the seeds) on the original planet? (yes/no, what was unclear?)")

    feedback6 = models.StringField(label="Was it clear that our intention was to study causal-effect relationships understanding?")
    
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
    form_fields = ['feedback' + str(x + 1) for x in range(6)]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage1, MyPage2]
