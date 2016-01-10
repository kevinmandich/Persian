import os
import time

from territories import *

class Game(object):
  '''
  The Game object keeps track of game-wide information.
  '''

  def __init__(self, players, ruleset='classic'):

    self.players = players
    self.ruleset = ruleset

    self.turn = 1
    self.wildlings = 0


class Map(dict):
  '''
  A graph where the nodes are Territory objects and the edges 
  represent ability to move between nodes.
  '''

  def __init__(self):




class Territory(object):
  '''
  A territory object is a node in the Map graph.
  '''

  def __init__(self, name, type_, supplies, castles, consolidation, port, garrison, owner, neighbors):

    self.name = name
    self.type = type_
    self.supplies = supplies
    self.castles = castles
    self.consolidation = consolidation
    self.port = port
    self.garrison = garrison
    self.owner = owner
    self.neighbors = neighbors