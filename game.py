import pdb
import os
import time
import copy
import logging
import sys

from collections import defaultdict
from random import shuffle

from territories import *
from fixed import *
from player import Player
from ai import *

log_level = logging.WARN # Change to debug, info, or warn
logging.basicConfig(stream=sys.stdout, level=log_level)
logger = logging.getLogger()

class Game(object):
  '''
  The Game object is the engine which keeps track of the game state
  and provides a means of running the game. Base class if a defaultdict
  of dicts.
  '''

  def __init__(self, players, ruleset='classic'):
    self.players = players
    self.num_players = len(players)
    self.ruleset = ruleset

    self.houses         = PLAYER_MAP              # dict
    self.order_tokens   = ORDER_TOKENS            # list of dicts
    self.supply_map     = SUPPLY_MAP              # dict
    self.supply_limits  = STARTING_SUPPLY_LIMITS  # dict
    self.supply_loads   = STARTING_SUPPLY_LOADS   # dict
    self.victory        = STARTING_VICTORY        # dict
    self.influence      = STARTING_INFLUENCE      # dict of dicts

    self.winner = None
    self.leader = None
    self.phase = None
    self.no_raid_orders = 0
    self.no_support_orders = 0
    self.no_defense_orders = 0
    self.no_consolidate_orders = 0
    self.no_march_plus_one_orders = 0

    # 1 Make the board (map)
    self.map = Map(copy.deepcopy(territories))

    # 2. Prepare the Wildling Deck and Wildling Threat
    # Token: Shuffle the Wildling cards to form a deck. Place this deck
    # on the space provided at the top of the game board. Then place the
    # Wildling threat token on the 2 position of the wildlings track
    self.wildlings = 2 # wildling threat token starts on the 2 position
    shuffle(WILDLING_CARDS)
    self.wildling_cards = WILDLING_CARDS

    # 3. Prepare the Westeros Decks: Separate the Westeros
    # cards into decks according to their roman numeral (I, II, or III).
    # Shuffle each deck and place them separately facedown next to
    # the game board.
    { shuffle(deck) for deck in WESTEROS_CARDS.itervalues() }
    self.westeros_cards = WESTEROS_CARDS
    self.revealed_westeros_cards = []

    # 4. Place the Neutral Force Tokens: First collect the
    # Neutral Force tokens marked with the correct range of
    # players. Then place those tokens on the areas of the game
    # board matching the name on each token.


    # 5. Place Game Round Marker: Place the Game Round
    # marker on the 1 position of the Round track.
    self.game_round_marker = 1

    # 6. Determine Player Houses: Each player now selects which
    # House he wishes to control during the game (Stark, Lannister,
    # Greyjoy, Tyrell, Baratheon, or Martell). Alternatively, players
    # may randomly determine which House each player will control.
    # When playing a game with fewer than six players, some Houses
    # are not eligible to be played, see page 28.
    self.assign_houses()
    self.houses_dict = { p.house : p for p in self.players }
    self.players_dict = { p.house : p for p in self.players } #combine with above

    # 7. Gather House Materials: Each player gathers all
    # materials belonging to his House. These are: 1 player screen,
    # 7 House cards, 15 Order tokens, 1 Supply token, 3 Influence
    # tokens, 1 Victory Point token, 1 Garrison token, and all
    # plastic units of his color (do not take any House-specific
    # Power tokens yet).

    self.throne_holder  = self.influence['iron throne'][1]
    self.sword_holder   = self.influence['fiefdom'][1]
    self.raven_holder   = self.influence['kings court'][1]

    # 8. Place Influence, Victory and Supply Tokens: Each player
    # places his Victory, Supply, and Influence tokens on the game
    # board tracks as instructed by his player screen. Unlike the
    # Influence tracks, more than one House may share the same
    # position on the Victory and Supply tracks.
    # If playing with fewer than six players, slide every Influence
    # token to the left (towards the 1 position) on each Influence
    # track to fill any leftward empty position (in other words, the
    # highest numbered positions on each track remains empty
    # and unused in games with fewer than six players). The Setup
    # Diagram on page 5 illustrates how Influence tokens have been
    # shifted left in a four-player game.
    # The Houses occupying each 1 (i.e., left-most) position on each
    # Influence track now claim the pictured Dominance token for
    # that track (the Iron Throne, the Valyrian Steel Blade, or the
    # Messenger Raven token).
    # 9. Place Units: Each player then places all of his starting
    # units on the game board according to the instructions on his
    # player screen.
    # 10. Place Garrison Tokens: Each player places his Garrison
    # token on his home area (matching the area name on the token).
    # 11. Gather Power Tokens: Place all Power tokens (for
    # all Houses) in a central pile. This pile of Power tokens is
    # referred to as the 'Power Pool." Each player then takes five
    # Power tokens matching his House from the Power Pool.

  def __str__(self):
    s = '\nTurn:\n  {}'.format(self.game_round_marker)
    s += '\n\nPhase:\n  {}'.format(self.phase)
    s += '\n\nPlayers:'
    for k, v in self.players_dict.iteritems():
      s += '\n  {}: {} ... AI module: {}'.format(v.name, v.house, v.ai)
    if self.winner:
      s += '\n\nWinner:\n  {}'.format(self.winner)
    else:
      s += '\n\nLeader:\n  {}'.format(self.leader)
    s += '\n\nWildlings:\n  {}'.format(self.wildlings)
    s += '\n\nInfluence:'
    for influence in self.influence:
      s += '\n  {}:'.format(influence)
      for place, player in self.influence[influence].iteritems():
        s += ', {}: {}'.format(place, player)
    s += '\n\nOwned Territories:'
    ot = self.map.owned_territories(self.players)
    for house in ot:
      s += '\n  ' + house + ': '
      s += ", ".join(ot[house])
    return s


  def assign_houses(self):
    shuffle(self.houses)
    for index in self.houses:
      self.players[index].house = self.houses[index]


  def tick(self):
    if self.game_round_marker > 1:
      self.westeros_phase()

    self.planning_phase()
    self.action_phase()
    self.clear()
    self.game_round_marker += 1

  def clear(self):
    for t in territories.itervalues():
      t.order_token = None

  def reconcile_supply(self):

    def over_supply_limit(house):
      logger.debug('house: {}'.format(house))
      limits = sorted(self.supply_map[self.supply_limits[house]], reverse=True)
      logger.debug('limits = {}'.format(limits))
      loads = sorted(self.supply_loads[house], reverse=True)
      logger.debug('loads = {}'.format(loads))
      if len(loads) > len(limits):
        logger.debug('over supply limit!')
        return 1
      for i in range(len(loads)):
        if loads[i] > limits[i]:
          logger.debug('over supply limit!')
          return 1
      return 0

    self.supply_limits = self.map.owned_supplies(self.players) # reset supply limits
    for house in self.houses_dict:
      if over_supply_limit(house):
        self.supply_loads[house] = self.houses_dict[house].reconcile_supply_limit(self)

  def bid(self, influence):
    bids = {}
    for house in self.houses_dict:
      bids[house] = self.houses_dict[house].bid_on_influence(self, influence) # { 'tyrell':3, 'greyjoy':5, ... }
    bids = sorted(zip(bids.values(),bids.keys()), reverse=True)

    # discard tokens
    for bid in bids:
      self.players_dict[bid[1]].power_tokens -= bid[0]

    return bids

  def bid_influence(self):

    def reconcile_ties(tying_houses):
      iron_throne_holder = self.houses_dict[self.influence['iron throne'][1]]
      return iron_throne_holder.determine_bid_tie_order(self, tying_houses)

    for influence in self.influence:
      bids = self.bid(influence)

      index = 0
      new_positions = []
      while True:
        tying_houses = []
        if bids[index][0] == bids[index+1][0]:
          tying_houses.extend([bids[index][1], bids[index+1][1]])
          while True:
            index += 1
            if index >= len(bids) - 1:
              new_positions.extend(reconcile_ties(tying_houses))
              break
            if bids[index][0] == bids[index+1][0]:
              tying_houses.append(bids[index+1][1])
            else:
              new_positions.extend(reconcile_ties(tying_houses))
              break
        else:
          new_positions.append(bids[index][1])
        index += 1
        if index == len(bids) - 1:
          new_positions.append(bids[index][1])
          break
        if index > len(bids) - 1:
          break
      for i in self.influence[influence]:
        self.influence[influence][i] = new_positions[i-1]

  def consolidate_power(self):
    # gettin' paid
    tokens_to_allocate = self.map.owned_consolidation(self.players)
    for house, tokens in tokens_to_allocate.iteritems():
      player = self.houses_dict[house]
      if tokens + player.power_tokens + player.map_power_tokens > 20:
        player.power_tokens = 20
      else:
        player.power_tokens += tokens

  ### WESTEROS PHASE ###
  def westeros_phase(self):
    self.phase = 'Westeros'
    # if game round marker = 10 find winner/end game
    if self.game_round_marker >= 10:
      self.check_winner()
      return

    # Reveal top 3 westeros
    for num in self.westeros_cards:
      card = self.draw_card(num)
      self.revealed_westeros_cards.append(card)

    # Advance wildling track
    for card in self.revealed_westeros_cards:
      if card in ['raven_holder', 'throne_holder', 'nothing', \
        'no_raid_orders', 'no_support_orders', 'no_defense_orders', \
        'no_consolidate_orders', 'no_march_plus_one_orders']:
        self.wildlings += 1

    if self.wildlings >= 12:
      self.wildlings_attack()

    # resolve 3 westeros cards
    for i, card in enumerate(self.revealed_westeros_cards):
      self.resolve_card(card, i+1)

    self.revealed_westeros_cards = []

  def draw_card(self, num):
    card = self.westeros_cards[num][0]
    self.westeros_cards[num].rotate(-1)
    return card

  def resolve_card(self, card, num):
    if card == 'muster':
      pass
    if card == 'supply':
      self.reconcile_supply()
    if card == 'bid':
      self.bid_influence()
    if card == 'consolidate':
      self.consolidate_power()
    if card == 'raven_holder':
      pass
    if card == 'sword_holder':
      pass
    if card == 'throne_holder':
      pass
    if card == 'wildlings':
      self.wildlings_attack()
    if card == 'shuffle': # draw the respective card again
      shuffle(self.westeros_cards[num])
      card = self.draw_card(num)
      self.resolve_card(card, num)
    if card == 'nothing':
      pass
    if card == 'no_raid_orders':
      self.no_raid_orders = 1
    if card == 'no_support_orders':
      self.no_support_orders = 1
    if card == 'no_defense_orders':
      self.no_defense_orders = 1
    if card == 'no_consolidate_orders':
      self.no_consolidate_orders = 1
    if card == 'no_march_plus_one_orders':
      self.no_march_plus_one_orders = 1
    return None

  def wildlings_attack(self):
    wildling_strength = self.wildlings

    # Bid
    bids = self.bid('wildling attack') #influence parameter?

    night_watch_strength = sum([bid[0] for bid in bids])

    # Calculate victory
    wildling_victory = night_watch_strength < wildling_strength

    if wildling_victory:
      self.wildlings = max(0, self.wildlings - 2)
    else:
      self.wildlings = 0

    # Revolve attack
    wildling_card = self.wildling_cards.pop()
    self.resolve_wildling_card(wildling_card, wildling_victory, bids)
    self.wildling_cards.append(wildling_card)

  def resolve_wildling_card(self, card, wildling_victory, bids):
    lowest_bidder = bids[-1][1]
    highest_bidder = bids[0][1]

    if card == 'skinchanger_scout':
      # -2 for everyone, 0 for lowest
      if wildling_victory:
        self.players_dict[lowest_bidder].power_tokens = 0
        for p in self.players:
          p.power_tokens = max(0, p.power_tokens - 2)
      # highest bidder keeps his tokens
      else:
        self.players_dict[highest_bidder].power_tokens += bids[0][0]

  ### WESTEROS PHASE END ###

  def planning_phase(self):
    logger.info('Planning Phase')
    self.phase = 'Planning'
    for player in self.players:
      plans = player.move(self)
      ## TODO break out
      for plan in plans:
        self.map.territories[plan['source']].order_token = plan['data']['order']

  def action_phase(self):
    logger.info('Action Phase')
    self.phase = 'Action'

    self.resolve_orders('Raid', self.resolve_raid)
    self.resolve_orders('March', self.resolve_march)
    self.resolve_orders('Consolidate', self.resolve_consolidate)

    # Todo move inside march phase
    winner = self.check_winner()
    if winner:
      return

  def resolve_orders(self, action_phase, phase_resolver):
    action_order = self.influence['iron throne']
    while len(self.map.territories_with_order(action_phase)) > 0:
      for i in range(1, self.num_players + 1):
        player_name = action_order[i]
        player = self.players_dict[player_name]

        if len(self.map.territories_for(player, action_phase)) > 0:

          plans = player.move(self, action_phase=action_phase)
          logger.debug('---------')
          for plan in plans:
            logger.debug("{} {}".format(player_name, plan['action']))
            phase_resolver(plan, player)


            self.map.territories[plan['source']].order_token = None

  def resolve_consolidate(self, plan, player):
    t = territories[plan['source']]
    if plan['data']['type'] == 'consolidation':
      power_tokens = t.consolidation + 1
      player.power_tokens += power_tokens
      logger.debug("{} has {} power".format(player.name, player.power_tokens))
    elif plan['data']['type'] == 'muster':
      pass # TODO

  def resolve_raid(self, plan, player):
    t1 = territories[plan['source']]
    t2 = territories.get(plan['data']['target'])

    if t2 and t2.order_token:
      if t2.order_token['type'] in ['Raid', 'Support']:
        logger.debug("{} loses order {}".format(t2.owner, t2.order_token['type']))
        t2.order_token = None
      elif t2.order_token == 'Consolidate':
        logger.debug("{} loses order {} and power token".format(t2.owner, t2.order_token['type']))
        t2.order_token = None
        players_dict[t1.owner].power_tokens += 1
        if players_dict[t2.owner].power_tokens > 0:
          players_dict[t2.owner].power_tokens -= 1
      elif t2.order_token['type'] == 'Defense' and t1.order_token['stars'] > 0:
        logger.debug("{} loses order {}".format(t2.owner, t2.order_token['type']))
        t2.order_token = None
    else:
      logger.debug('Raid useless')

  def resolve_march(self, plan, player):
    t1 = territories[plan['source']]
    t2 = territories.get(plan['data']['target'])
    if t2:
      self.battle(t1,t2, plan['data'].get('leave_token'))
    else:
      logger.debug('March useless')

  def battle(self, t1, t2, leave_token):
      defend_power = t2.knight * 2 + t2.footmen + t2.ships + t2.castles
      attack_power = t1.knight * 2 + t1.footmen + t1.ships + t1.siege

      # TODO ask others to join sides
      for t in t2.neighbors:
        support_t = self.map.territories[t]
        if support_t.owner != None and support_t.owner == t2.owner and support_t.order_token and support_t.order_token['type'] == 'Support':
          defend_power += support_t.knight * 2 + support_t.footmen + support_t.ships
        elif support_t.owner == t1.owner and support_t.order_token and support_t.order_token['type'] == 'Support':
          attack_power += support_t.knight * 2 + support_t.footmen + support_t.ships

      #TODO influence on ties, cards, tides of battle
      if attack_power > defend_power:
        logger.debug("{} beat {} and won {} castles".format(t1.owner, t2.owner, t2.castles))
        t2.owner = t1.owner
        t2.knight = t1.knight
        t2.footmen = t1.footmen
        t2.ships = t1.ships
        t2.siege = t1.siege
        t1.knight = 0
        t1.footmen = 0
        t1.ships = 0
        t1.siege = 0
        attacker = self.players_dict[t1.owner]
        if leave_token and attacker.power_tokens > 0:
          t1.power_token = 1
          attacker.power_tokens -= 1
      else:
        logger.debug("{} lost to {}".format(t1.owner, t2.owner))

  def print_power_tokens(self):
    for house, player in self.houses_dict.iteritems():
      logger.debug('{} : {} power tokens'.format(house, player.power_tokens))


  def check_winner(self):
    winner = None
    self.leader = None
    max_castles = 0

    player_dict = {}
    for p in self.players:
      player_dict[p.house] = 0

    for t in self.map.territories.itervalues():
      if t.owner:
        player_dict[t.owner] += 1

    for p, count in player_dict.iteritems():
      if count > max_castles:
        max_castles = count
        self.leader = p

    if self.game_round_marker > 9 or max_castles >= 7:
      winner = self.leader

    self.winner = winner
    return winner


  def run(self):
    while self.game_round_marker < 10 and not self.winner:
      self.tick()

    return self.players_dict[self.check_winner()]





class Map(defaultdict):
  '''
  A graph where the nodes are Territory objects and the edges
  represent ability to move between nodes.
  '''

  def __init__(self, territories):

    defaultdict.__init__(self, dict)
    self.territories = territories
    self.create()

  def __str__(self):
    '''
    logger out a formatted representation of each Territory
    and its neighbors
    '''
    s = ""
    for t1 in self:
      s += '\n' + t1
      for t2 in self[t1]:
        s += '    {} - {}'.format(t2, self[t1][t2])
    return s

  def create(self):
    '''
    Create the graph
    '''

    for name, t in self.territories.iteritems():
      for neighbor in t.neighbors:
        n = self.territories[neighbor]
        self[t.name][n.name] = t.type + '-' + n.type
        self[n.name][t.name] = n.type + '-' + t.type

  def territories_for(self, player, action_phase=None, planning=False):
    player_territories = []
    for t in self.territories.itervalues():
      if t.owner and t.owner == player.house:
        if action_phase:
          if t.order_token and t.order_token['type'] == action_phase:
            logger.debug(t.order_token['type'])
            player_territories.append(t)
        elif planning:
          if t.has_unit():
            player_territories.append(t)
        else:
          player_territories.append(t)

    return player_territories

  def territories_with_order(self, action_phase):
    territories = []
    for t in self.territories.itervalues():
      if t.order_token and t.order_token['type'] == action_phase:
        territories.append(t)

    return territories

  def owned_territories(self, players):
    ot = { p.house : [] for p in players }
    for t in self.territories.itervalues():
      if t.owner:
        ot[t.owner].append(t.name)
    return ot

  def owned_supplies(self, players):
    sl = { p.house : 0 for p in players }
    for t in self.territories.itervalues():
      if t.owner:
        sl[t.owner] += t.supplies
    return sl

  def owned_consolidation(self, players):
    c = { p.house : 0 for p in players }
    for t in self.territories.itervalues():
      if t.owner:
        c[t.owner] += t.consolidation
    return c


if __name__ == '__main__':

  ai_module = SimpleAI

  players = [
    Player('simple1',   ai_module()),
    Player('simple2',   ai_module()),
    Player('simple3',   ai_module()),
    Player('simple4',   ai_module()),
    Player('simple5',   ai_module()),
    Player('human',     HumanAI()),
  ]
  g = Game(players=players, ruleset='classic')
  g.run()
