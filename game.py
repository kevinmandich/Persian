import os
import time

from territories import *

class Game(object):
  '''
  The Game object keeps track of the game state.
  '''

  def __init__(self, players, ruleset='classic'):

    self.players = players
    self.ruleset = ruleset
    self.map = Map()
    self.turn = 1
    self.phase = None
    self.wildlings = 0
    self.order_tokens = ORDER_TOKENS

    self.territories = []

    # self.supply_track =

    self.winner = None


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

      for t in self.territories:
        player_dict[t.owner.name] += 1

      for p, count in player_dict.iter_items():
        if count > max_castles:
          leader = p

      if self.turn > 9:
        winner = leader
      else if max_castles >= 7:
        winner = leader

      self.winner = winner
      return winner


    def play(self):
      while self.turn < 10 and not self.winner:
        self.tick()

    ORDER_TOKENS = [
    {'type': 'Raid', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Raid', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Raid', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'March', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'March', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'March', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Defense', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Defense', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Defense', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Support', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Support', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Support', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Consolidate', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Consolidate', 'value': 0, 'stars': 0, 'valid': True},
    {'type': 'Consolidate', 'value': 0, 'stars': 0, 'valid': True},
    ]




class Map(dict):
  '''
  A graph where the nodes are Territory objects and the edges
  represent ability to move between nodes.
  '''

  def __init__(self):




