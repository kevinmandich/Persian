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

    self.turn = 1
    self.phase = None
    self.wildlings = 0

    self.supply_track = 


class Map(dict):
  '''
  A graph where the nodes are Territory objects and the edges 
  represent ability to move between nodes.
  '''

  def __init__(self):




