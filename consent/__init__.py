from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
        Cons_1 = models.StringField(
        choices=["Yes"],
        label='By choosing Yes option, I acknowledge that I am 18 or older, that I am a fluent speaker of English, that I have read this consent form, and that I agree to take part in the research.',
        widget=widgets.RadioSelectHorizontal)

        Cons_2 = models.StringField(
        choices=["Yes"],
        label='By choosing Yes option,I agree to participate in studies or experimental assesment of decision making',
        widget=widgets.RadioSelectHorizontal)
        
        Cons_3 = models.StringField(blank=True,
        choices=["Yes", "No"],
        label='Optionally, agreement to transfer data to the cooperation partners: I request and herewith simultaneously consent to data transfer from the MPI for Biological Cybernetics encrypted database to the project related collaborators:',
        widget=widgets.RadioSelect)

        Cons_4 = models.StringField(blank=True,
        choices=["Yes",],
        label='inside of the Max-Planck-Society and affiliated research institutes',
        widget=widgets.RadioSelect)

        Cons_5 = models.StringField(blank=True,
        choices=["Yes",],
        label='at partnering institutions (for example, the University of Tübingen, New York University)',
        widget=widgets.RadioSelect)

    

# FUNCTIONS
# PAGES

class consentpage(Page):
    form_model = 'player'
    form_fields = ['Cons_1'] 
class dataprotection(Page):
    form_model = 'player'
    form_fields = ['Cons_2'] +['Cons_3'] +['Cons_4'] +['Cons_5'] 

page_sequence = [consentpage,dataprotection]