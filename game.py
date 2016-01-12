import os
import time
import copy

from collections import defaultdict
from random import shuffle

from territories import *
from fixed import *
from player import Player

class Game(object):
  '''
  The Game object is the engine which keeps track of the game state
  and provides a means of running the game. Base class if a defaultdict
  of dicts.
  '''

  def __init__(self, players, ruleset='classic'):

    self.players = players
    self.players_dict = { p.name : p for p in self.players }
    self.ruleset = ruleset
    self.map = Map(copy.deepcopy(territories))

    self.winner = None
    self.turn = 0
    self.phase = None
    self.wildlings = 0
    self.no_raid_orders = 0
    self.no_support_orders = 0
    self.no_defense_orders = 0
    self.no_consolidate_orders = 0
    self.no_march_plus_one_orders = 0

    self.houses         = PLAYER_MAP              # dict
    self.order_tokens   = ORDER_TOKENS            # list of dicts
    self.supply_map     = SUPPLY_MAP              # dict
    self.supply_limits  = STARTING_SUPPLY_LIMITS  # dict
    self.supply_loads   = STARTING_SUPPLY_LOADS   # dict
    self.victory        = STARTING_VICTORY        # dict
    self.influence      = STARTING_INFLUENCE      # dict of dicts

    self.throne_holder  = self.influence['iron throne'][1]
    self.sword_holder   = self.influence['fiefdom'][1]
    self.raven_holder   = self.influence['kings court'][1]

    shuffle(WILDLING_CARDS)
    { shuffle(deck) for deck in WESTEROS_CARDS.itervalues() }
    self.wildling_cards = WILDLING_CARDS
    self.westeros_cards = WESTEROS_CARDS

    self.assign_houses()
    self.houses_dict = { p.house : p for p in self.players }

  def __str__(self):
    s = '\nPlayers:'
    for k, v in self.players_dict.iteritems():
      s += '\n  {}: {} ... AI module: {}'.format(k, v.house, v.ai)
    s += '\n\nWinner:\n  {}'.format(self.winner)
    s += '\n\nRuleset:\n  {}'.format(self.ruleset)
    s += '\n\nTurn:\n  {}'.format(self.turn)
    s += '\n\nPhase:\n  {}'.format(self.phase)
    s += '\n\nWildlings:\n  {}'.format(self.wildlings)
    s += '\n\nInfluence:'
    for influence in self.influence:
      s += '\n  {}:'.format(influence)
      for place, player in self.influence[influence].iteritems():
        s += '\n    {}: {}'.format(place, player)
    return s


  def assign_houses(self):
    shuffle(self.houses)
    for index in self.houses:
      self.players[index].house = self.houses[index]


  def tick(self):
    self.turn += 1
    # print 'turn {}'.format(self.turn)
    if self.turn > 1:
      self.westeros_phase()

    self.planning_phase()
    self.action_phase()
    self.clear()

  def clear(self):
    for t in territories.itervalues():
      t.order_token = None

  def reconcile_supply(self):

    def over_supply_limit(house):
      limits = sorted(self.supply_map[self.supply_limits[house]], reverse=True)
      print 'limits = {}'.format(limits)
      loads = sorted(self.supply_loads[house], reverse=True)
      print 'loads = {}'.format(loads)
      if len(loads) > len(limits):
        print 'over supply limit!'
        return 1
      for i in range(len(loads)):
        if loads[i] > limits[i]:
          print 'over supply limit!'
          return 1
      return 0

    self.supply_limits = self.map.owned_supplies(self.players)
    for house in self.houses_dict:
      if over_supply_limit(house):
        self.supply_loads[house] = self.houses_dict[house].reconcile_supply_limit(self, )

  def westeros_phase(self):
    self.phase = 'Westeros'

    def draw_card(num):
      card = self.westeros_cards[num][0]
      self.westeros_cards[num].rotate(-1)
      return card

    def resolve_card(card, num):
      if card == 'muster':
        pass
      if card == 'supply':
        self.reconcile_supply()
      if card == 'bid':
        pass
      if card == 'consolidate':
        pass
      if card == 'raven_holder':
        pass
      if card == 'sword_holder':
        pass
      if card == 'throne_holder':
        pass
      if card == 'wildlings':
        pass
      if card == 'shuffle': # draw the respective card again
        shuffle(self.westeros_cards[num])
        draw_card(num)
        resolve_card(card, num)
      if card == 'nothing':
        pass # actually pass
      if num == 3:
        self.no_raid_orders = 1 if card == 'no_raid_orders' else 0
        self.no_support_orders = 1 if card == 'no_support_orders' else 0
        self.no_defense_orders = 1 if card == 'no_defense_orders' else 0
        self.no_consolidate_orders = 1 if card == 'no_consolidate_orders' else 0
        self.no_march_plus_one_orders = 1 if card == 'no_march_plus_one_orders' else 0
      return None

    for num in self.westeros_cards:
      card = draw_card(num)
      resolve_card(card, num)




  def planning_phase(self):
    # print 'Planning Phase'
    self.phase = 'Planning'
    for player in self.players:
      plans = player.move(self)
      ## TODO break out
      for plan in plans:
        territories[plan['source']].order_token = plan['data']['order']

  def action_phase(self):
    # print 'Action Phase'
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
      for i in range(1,7):
        player_name = action_order[i]
        player = self.players_dict[player_name]

        if len(self.map.territories_for(player, action_phase)) > 0:

          plans = player.move(self, action_phase=action_phase)
          # print '---------'
          for plan in plans:
            # print "{} {}".format(player_name, plan['action'])
            phase_resolver(plan, player)


          territories[plans[0]['source']].order_token = None


  def resolve_consolidate(self, plan, player):
    t = territories[plan['source']]
    if plan['data']['type'] == 'consolidation':
      power_tokens = t.consolidation + 1
      player.power_tokens += power_tokens
      # print "{} has {} power".format(player.name, player.power_tokens)
    elif plan['data']['type'] == 'muster':
      pass# print 'todo'

  def resolve_raid(self, plan, player):
    t1 = territories[plan['source']]
    t2 = territories.get(plan['data']['target'])

    if t2:
      if t2.order_token['type'] in ['Raid', 'Support']:
        # print "{} loses order {}".format(t2.owner, t2.order_token['type'])
        t2.order_token = None
      elif t2.order_token == 'Consolidate':
        # print "{} loses order {} and power token".format(t2.owner, t2.order_token['type'])
        t2.order_token = None
        players_dict[t1.owner].power_tokens += 1
        if players_dict[t2.owner].power_tokens > 0:
          players_dict[t2.owner].power_tokens -= 1
      elif t2.order_token['type'] == 'Defense' and t1.order_token['stars'] > 0:
        # print "{} loses order {}".format(t2.owner, t2.order_token['type'])
        t2.order_token = None
    else:
      pass# print 'Raid useless'

  def resolve_march(self, plan, player):
    t1 = territories[plan['source']]
    t2 = territories.get(plan['data']['target'])
    if t2:
      self.battle(t1,t2, plan['data'].get('leave_token'))
    else:
      pass# print 'March useless'

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
        # print "{} beat {} and won {} castles".format(t1.owner, t2.owner, t2.castles)
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
        pass# print "{} lost to {}".format(t1.owner, t2.owner)


  def check_winner(self):
    winner = None
    leader = None
    max_castles = 0

    player_dict = {}
    for p in self.players:
      player_dict[p.name] = 0

    for t in self.map.territories.itervalues():
      if t.owner:
        player_dict[t.owner] += 1

    for p, count in player_dict.iteritems():
      if count > max_castles:
        max_castles = count
        leader = p

    if self.turn > 9 or max_castles >= 7:
      winner = leader

    self.winner = winner
    return winner


  def run(self):
    while self.turn < 10 and not self.winner:
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
    Print out a formatted representation of each Territory
    and its neighbors
    '''

    for t1 in self:
      print '\n', t1
      for t2 in self[t1]:
        print '    {} - {}'.format(t2, self[t1][t2])

  def create(self):
    '''
    Create the graph
    '''

    for name, t in self.territories.iteritems():
      for neighbor in t.neighbors:
        n = self.territories[neighbor]
        self[t.name][n.name] = t.type + '-' + n.type
        self[n.name][t.name] = n.type + '-' + t.type

  def territories_for(self, player, action_phase=None):
    player_territories = []
    for t in self.territories.itervalues():
      if t.owner and t.owner == player.name:
        if action_phase:
          if t.order_token and t.order_token['type'] == action_phase:
            # print t.order_token['type']
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


if __name__ == '__main__':

  players = [
    Player(name='Kevin'),
    Player(name='Will'),
    Player(name='Scot'),
    Player(name='Vidur'),
    Player(name='Andrew'),
    Player(name='Paul'),
  ]
  g = Game(players=players, ruleset='classic')













