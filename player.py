from fixed import *


class Player(object):
  '''
  A player object is a player in the game.
  '''

  def __init__(self):

    self.name          = 'Defaut Player'
    self.order_tokens  = ORDER_TOKENS
    self.ship_units    = 5
    self.footmen_units = 5
    self.knights_units = 5
    self.siege_units   = 2

  def move(self, game):
    if game.phase == 'Planning':
      self.planning_move(game)
    elif game.phase == 'Action':
      self.action_move(game)

  def action_move(self, game):
    game
    #TODO

  def planning_move(self, game):
    game
    #TODO

players = [

]



