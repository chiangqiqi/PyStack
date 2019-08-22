'''
    Various constants used in DeepStack.
'''

from helper_classes import Players
from helper_classes import NodeTypes
from helper_classes import Actions

# hand_count
HC = 1326 # 52*51/2


# the number of players in the game
players_count = 2
# the number of betting rounds in the game
streets_count = 4
# the number of card suits in the deck
suit_count = 4
# the number of card ranks in the deck
rank_count = 13
# the total number of cards in the deck
card_count = suit_count * rank_count
# the number of public cards dealt in the game (revealed after the first betting round)
board_card_count = [0, 3, 4, 5]
hand_card_count = 2
hand_count = 1326 # 52*51/2

# IDs for each player and chance
players = Players()
players.chance = -1
players.P1 = 0
players.P2 = 1

# IDs for terminal nodes (either after a fold or call action) and
# nodes that follow a check action
node_types = NodeTypes()
node_types.terminal_fold = -2 # terminal node following fold
node_types.terminal_call = -1 # terminal node following call
node_types.check = -1 # node for the chance player
node_types.chance_node = 0 # node following check
node_types.inner_node = 1 # any other node

# IDs for fold and check/call actions
actions = Actions()
actions.fold = -2
actions.ccall = -1 # (check/call)
actions.raise_ = -3

# variables needed for CFR+
regret_epsilon = 1e-8
max_number = 999999
