from otree.api import *
import random
import pandas
import json

class C(BaseConstants):
    NAME_IN_URL = 'rockpaperscissors'
    HISTORY_TEMPLATE = 'rockpaperscissors/history.html'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15
    CHOICES = ['Rock', 'Paper', 'Scissors']
    BOTS_PER_GROUP = 1
    AGENTS_PER_GROUP = BOTS_PER_GROUP + 1
    # draw_1 = random.sample(CHOICES, len(CHOICES))
    # draw_2 = random.sample(CHOICES, len(CHOICES))
    # draw_3 = random.sample(CHOICES, len(CHOICES))
    draw_1 = random.choices(CHOICES,k=len(CHOICES))
    draw_2 = random.choices(CHOICES, k=len(CHOICES))
    draw_3 = random.choices(CHOICES, k=len(CHOICES))
    strategy_with_memory={'Rock':{"Paper": draw_1[0],'Rock':draw_1[1], "Scissors":draw_1[2]}, 
    'Paper':{"Paper": draw_2[0],'Rock':draw_2[1], "Scissors":draw_2[2]}, 
    'Scissors':{"Paper": draw_3[0],'Rock':draw_3[1], "Scissors":draw_3[2]}}
    strategy_with_memory_for_check={'Rock'[0]:{"Paper"[0]: draw_1[0][0],'Rock'[0]:draw_1[1][0], "Scissors"[0]:draw_1[2][0]}, 
 'Paper'[0]:{"Paper"[0]: draw_2[0][0],'Rock'[0]:draw_2[1][0], "Scissors"[0]:draw_2[2][0]}, 
 'Scissors'[0]:{"Paper"[0]: draw_3[0][0],'Rock'[0]:draw_3[1][0], "Scissors"[0]:draw_3[2][0]}}
    strategy_as_table = pandas.DataFrame(columns=['edge','value'])
    for source, dest in strategy_with_memory_for_check.items():
        for key, value in dest.items():
            strategy_as_table.loc[len(strategy_as_table)+1]=[source+value, key, ]
    for i,g in enumerate(set(strategy_as_table[strategy_as_table.duplicated(['edge'])]['edge'])):
        sep=""
        strategy_as_table.loc[strategy_as_table['edge'].isin([g]),"value"]=sep.join(list(strategy_as_table[strategy_as_table['edge'] == g]['value']))




class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        for i in range(C.BOTS_PER_GROUP):
            MyBot.create(player=p, agent_id=i + 1)



class Group(BaseGroup):
    is_draw = models.BooleanField()


class Player(BasePlayer):
    hand = models.StringField(choices=C.CHOICES)
    opponent_hand = models.StringField()
    result = models.StringField()
    agent_id = models.IntegerField(initial=1)
    stored = models.StringField()
    points = models.IntegerField()

class MyBot(ExtraModel):
    player = models.Link(Player)
    hand = models.StringField(choices=C.CHOICES)
    opponent_hand = models.StringField()
    result = models.StringField()
    payoff = models.CurrencyField()
    agent_id = models.IntegerField()


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'payoff', 'automaton']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, p.round_number, p.id_in_group, p.payoff, C.strategy_with_memory]




def set_winner(player: Player):
    bots = MyBot.filter(player=player)
    if player.round_number == 1:
        player.participant.vars['strategy_with_memory']=C.strategy_with_memory
    for bot in bots:
        if player.round_number == 1:
            bot.hand = random.choice(C.CHOICES)
            bot_hand= bot.hand 

        else:
            prev_player = player.in_round(player.round_number - 1)
            bot.hand = C.strategy_with_memory[prev_player.hand][prev_player.opponent_hand]
        bot_hand= bot.hand 
        bot.opponent_hand =  player.hand


    if player.hand == bot_hand:
        player.result = 'Draw'
    elif player.hand + bot_hand in 'ScissorsPaperRockScissors':
        player.result = 'Win'
    else:
        player.result = 'Loss'

    player.opponent_hand = bot_hand

def live_method(player, data):
    # player.stored = str(1)
    player.stored = json.dumps(data)

def count_score(player):
    store_array = json.loads(player.stored)
    reported_edges=[(v["id"], v['label']) for v in store_array]
    reported_edges_df = pandas.DataFrame(data=reported_edges,columns=['edge','value'])
    points = []
    for id in [v["id"] for v in store_array]:
        points.append(len(
            set(C.strategy_as_table.drop_duplicates().loc[C.strategy_as_table.drop_duplicates()['edge'].isin([id]),"value"].values) & 
            set(reported_edges_df.loc[reported_edges_df['edge'].isin([id]),"value"].values)))
    return (sum(points))




class Shoot(Page):
    form_model = 'player'
    form_fields = ['hand']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(past_players=player.in_all_rounds()[::-1][1:])

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_winner(player)

class WaitForBots(Page):
    """
    This is just for show, to make it feel more realistic.
    Also, note it's a Page, not a WaitPage.
    Removing this page won't affect functionality.
    """

    @staticmethod
    def get_timeout_seconds(player: Player):
        return random.randint(1, 1)

class DiagramTask(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    live_method = live_method
    def before_next_page(player: Player, timeout_happened):
        player.points = int(count_score(player))

class FinalResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        store_array = json.loads(player.stored)
        # return dict(past_players=[1,2,3,4,5][::-1])
        return dict(past_players=player.in_all_rounds(), 
        edges=[(i,v["id"], v['label']) for i,v in enumerate(store_array)],
        CompPlayer=[(i, row["edge"],row["value"]) for i,row in C.strategy_as_table.drop_duplicates().iterrows()]
        )



# class Results(Page):
#     @staticmethod
#     def is_displayed(player: Player):
#         return player.round_number == C.NUM_ROUNDS





page_sequence = [Shoot,  WaitForBots, DiagramTask, FinalResults,]
# Results


