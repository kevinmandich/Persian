from fixed import *
import random


class Player(object):
  '''
  A player object is a player in the game.
  '''

  def __init__(self, name, ai=None):

    self.name          = name
    self.house         = None
    self.order_tokens  = list(ORDER_TOKENS)
    self.ship_units    = 5
    self.footmen_units = 5
    self.knights_units = 5
    self.siege_units   = 2

    self.ai = ai

  def __str__(self):
    return 'Player class for player {} playing house {}'.format(self.name, self.house)

  def move(self, game):
    if game.phase == 'Planning':
      return self.planning_move(game)
    elif game.phase == 'Action':
      return self.action_move(game)

  def action_move(self, game):
    if self.ai:
      return self.ai.action_move(game)

  def planning_move(self, game):
    if self.ai:
      return self.ai.planning_move(game)
    else:
      my_territories = game.map.territories_for(self)
      plan_moves = []
      for t in my_territories:
        random.shuffle(self.order_tokens)
        order = self.order_tokens.pop()
        plan_moves.append({'action': 'planning', 'source': t.name, 'data': {'order': order}})

      return plan_moves


