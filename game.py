import os
import time

from collections import defaultdict
from random import shuffle

from territories import *
from fixed import *
from player import Player

class Game(object):
  '''
  The Game object is the engine which keeps track of the game state
  and provides a means of running the game.
  '''

  def __init__(self, players, ruleset='classic'):

    self.players = players
    self.players_dict = {}

    for p in self.players:
      self.players_dict[p.name] = p

    self.ruleset = ruleset
    self.map = Map(territories)

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
    self.wildling_cards = shuffle(WILDLING_CARDS)
    self.throne_holder  = self.influence['iron throne'][1]
    self.sword_holder   = self.influence['fiefdom'][1]
    self.raven_holder   = self.influence['kings court'][1]

    self.winner = None

    self.assign_houses()


  def assign_houses(self):

    shuffle(self.houses)
    for index in self.houses:
      self.players[index].house = self.houses[index]

    return None


  def tick(self):
    self.turn += 1
    print 'turn {}'.format(self.turn)
    if self.turn > 1:
      self.westeros_phase()

    self.planning_phase()
    self.action_phase()
    self.clear()

  def clear(self):
    for t in territories.itervalues():
      t.order_token = None

  def westeros_phase(self):
    self.phase = 'Westeros'
    #TODO
    # for player in self.players:
    #   player.move(self)

  def planning_phase(self):
    print 'Planning Phase'
    self.phase = 'Planning'
    for player in self.players:
      plans = player.move(self)
      ## TODO break out
      for plan in plans:
        territories[plan['source']].order_token = plan['data']['order']

  def action_phase(self):
    print 'Action Phase'
    self.phase = 'Action'

    self.resolve_orders('Raid', self.resolve_raid)
    # self.resolve_orders('March')
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

          for plan in plans:
            phase_resolver(plan, player)

          territories[plans[0]['source']].order_token = None


  def resolve_consolidate(self, plan, player):
    t = territories[plan['source']]
    if plan['data']['type'] == 'consolidation':
      power_tokens = t.consolidation + 1
      player.power_tokens += power_tokens
    elif plan['data']['type'] == 'muster':
      print 'todo'

  def resolve_raid(self, plan, player):
    t1 = territories[plan['source']]
    t2 = territories.get(plan['data']['target'])

    if t2:
      if t2.order_token['type'] in ['Raid', 'Support']:
        t2.order_token = None
      elif t2.order_token == 'Consolidate':
        t2.order_token = None
        players_dict[t1.owner].power_tokens += 1
        if players_dict[t2.owner].power_tokens > 0:
          players_dict[t2.owner].power_tokens -= 1
      elif t2.order_token['type'] == 'Defense' and t1.order_token['stars'] > 0:
        t2.order_token = None



  def resolve_march(self, plan, player):
    t = territories[plan['source']]




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

    return self.check_winner()





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













