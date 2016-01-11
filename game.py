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
    self.phase = 'Action'
    #eventually order players by influence

    #Resolve Raid
    #Resolve March
    #Resolve Consolidate

    for player in self.players:
      player.move(self)
      winner = self.check_winner()
      if winner:
        return

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

  def territories_for(self, player):
    player_territories = []
    for t in self.territories.itervalues():
      if t.owner and t.owner == player.name:
        player_territories.append(t)

    return player_territories


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













