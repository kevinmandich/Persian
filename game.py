import os
import time

from collections import defaultdict

from territories import *

class Game(object):
  '''
  The Game object keeps track of the game state.
  '''

  def __init__(self, players, ruleset='classic'):

    self.players = players
    self.ruleset = ruleset
    self.map = Map(territories)
    self.turn = 1
    self.phase = None
    self.wildlings = 0

    # self.supply_track =

    self.winner = None

  def instantiate(self):

    self.map.create()


  def assign_houses(self):

    return None


  def tick(self):
    if self.turn > 1:
      self.westeros_phase()

    self.planning_phase()
    self.action_phase()
    self.turn += 1

  def westeros_phase(self):
    self.phase = 'Westeros'
    #TODO
    # for player in self.players:
    #   player.move(self)

  def planning_phase(self):
    self.phase = 'Planning'
    for player in self.players:
      player.move(self)

  def action_phase(self):
    self.phase = 'Action'
    #eventually order players by influence
    for player in self.players:
      player.move(self)
      self.check_winner()


  def check_winner(self):
    winner = None
    leader = None
    max_castles = 0

    player_dict = {}
    for p in self.players:
      player_dict[p.name] = 0

    for t in self.territories:
      player_dict[t.owner.name] += 1

    for p, count in player_dict.iter_items():
      if count > max_castles:
        leader = p

    if self.turn > 9 or max_castles >= 7:
      winner = leader

    self.winner = winner


  def run(self):
    while self.turn < 10 and not self.winner:
      self.tick()




class Map(defaultdict):
  '''
  A graph where the nodes are Territory objects and the edges
  represent ability to move between nodes.
  '''

  def __init__(self, territories):

    defaultdict.__init__(self, dict)
    self.territories = territories

  def create(self):

    for t in self.territories.itervalues():
      for neighbor in t.neighbors:
        n = self.territories[neighbor]
        self[t][n] = t.type + '-' + n.type
        self[n][t] = n.type + '-' + t.type


if __name__ == '__main__':

  players = {0:'kevin',1:'will',2:'scot',3:'vidur',4:'andrew',5:'paul'}
  g = Game(players=players, ruleset='classic')
  g.instantiate()













