from collections import deque

__all__ = ['ORDER_TOKENS','STARTING_INFLUENCE','SUPPLY_MAP','STARTING_SUPPLY_LIMITS', \
           'STARTING_SUPPLY_LOADS','STARTING_VICTORY','PLAYER_MAP','WILDLING_CARDS', \
           'WESTEROS_CARDS']

ORDER_TOKENS = [
{'type': 'Raid', 'value': 0, 'stars': 0, 'valid': True},
{'type': 'Raid', 'value': 0, 'stars': 0, 'valid': True},
{'type': 'Raid', 'value': 0, 'stars': 1, 'valid': True},
{'type': 'March', 'value': -1, 'stars': 0, 'valid': True},
{'type': 'March', 'value': 0, 'stars': 0, 'valid': True},
{'type': 'March', 'value': 1, 'stars': 1, 'valid': True},
{'type': 'Defense', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Defense', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Defense', 'value': 2, 'stars': 1, 'valid': True},
{'type': 'Support', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Support', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Support', 'value': 2, 'stars': 1, 'valid': True},
{'type': 'Consolidate', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Consolidate', 'value': 1, 'stars': 0, 'valid': True},
{'type': 'Consolidate', 'value': 1, 'stars': 1, 'valid': True},
]

STARTING_INFLUENCE = {'iron throne': {1:'baratheon', 2:'lannister', 3:'stark', 4:'martell', 5:'greyjoy', 6:'tyrell'}, \
                      'fiefdom':     {1:'greyjoy', 2:'tyrell', 3:'martell', 4:'stark', 5:'baratheon', 6:'lannister'}, \
                      'kings court': {1:'lannister', 2:'stark', 3:'martell', 4:'baratheon', 5:'tyrell', 6:'greyjoy'}}

SUPPLY_MAP = {0:[2,2], 1:[3,2], 2:[3,2,2], 3:[3,2,2,2], 4:[3,3,2,2], 5:[4,3,2,2], 6:[4,3,2,2,2]}

PLAYER_MAP = {0:'stark',1:'tyrell',2:'martell',3:'lannister',4:'baratheon',5:'greyjoy'}

STARTING_SUPPLY_LIMITS = {'greyjoy':2,'tyrell':2,'martell':2,'lannister':2,'baratheon':2,'stark':1}

STARTING_SUPPLY_LOADS = {'greyjoy':[2],'tyrell':[2],'martell':[2],'lannister':[2],'baratheon':[2,2],'stark':[2]}

STARTING_VICTORY = {'greyjoy':1,'tyrell':1,'martell':1,'lannister':1,'baratheon':1,'stark':2}

WESTEROS_CARDS = { \
                  1:deque(['muster','muster','muster','supply','supply','supply','throne_holder','throne_holder','shuffle','nothing']), \
                  2:deque(['bid','bid','bid','consolidate','consolidate','consolidate','raven_holder','raven_holder','shuffle','nothing']), \
                  3:deque(['wildlings','wildlings','wildlings','sword_holder','sword_holder','no_raid_orders','no_defense_orders','no_support_orders','no_consolidate_orders','no_march_plus_one_orders']) \
                  }

# TODO add all 9 cards
# https://dl.dropboxusercontent.com/u/80803994/wildlings.png
WILDLING_CARDS = deque(['skinchanger_scout', 'massing_milkwater', 'king_beyond_the_wall', 'mammoth_riders', 'crow_killers', 'horde_descends', 'rattleshirt_raiders', 'silence_at_the_wall', 'prememptive_raid'])
