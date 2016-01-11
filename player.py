from fixed import *
import random


class Player(object):
  '''
  A player object is a player in the game.
  '''

  def __init__(self, name, ai=None):
    self.ai = ai

    self.name          = name
    self.house         = None
    self.order_tokens  = list(ORDER_TOKENS)
    self.ship_units    = 5
    self.footmen_units = 5
    self.knights_units = 5
    self.siege_units   = 2
    self.power_tokens  = 5 # start with 5

    self.ai = ai

  def __str__(self):
    return 'Player class for player {} playing house {}'.format(self.name, self.house)

  def move(self, game, action_phase=None):
    if game.phase == 'Planning':
      return self.planning_move(game)
    elif game.phase == 'Action':
      return self.action_move(game, action_phase=action_phase)

  def action_move(self, game, action_phase):
    return self.ai.action_move(game, self, action_phase)

  def planning_move(self, game):
    return self.ai.planning_move(game, self)




class RandomAi(object):
  def __init__(self):
    self


  def planning_move(self, game, player):
    my_territories = game.map.territories_for(player)
    plan_moves = []
    order_tokens = list(player.order_tokens)
    for t in my_territories:
      random.shuffle(order_tokens)
      order = order_tokens.pop()
      plan_moves.append({'action': 'planning', 'source': t.name, 'data': {'order': order}})

    return plan_moves

  def action_move(self, game, player, action_phase):
    territories_for_move = game.map.territories_for(player, action_phase)

    if action_phase == 'Raid':
      plan_moves = self.raid_move(game, player, territories_for_move)
    elif action_phase == 'March':
      plan_moves = self.march_move(game, player, territories_for_move)
    elif action_phase == 'Consolidate':
      plan_moves = self.consolidate_move(game, player, territories_for_move)

    return plan_moves


  def raid_move(self, game, player, my_territories):
    neighbors = []
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.order_token and neighbor.owner != player.name:
          neighbors.append(n)

    if len(neighbors) > 0:
      return [{'action': 'action', 'source': my_territories[0].name, 'data': {'target': neighbors.pop()}}]
    else:
      return [{'action': 'action', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def consolidate_move(self, game, player, my_territories):
    return [{'action': 'action', 'source': my_territories[0].name, 'data': {'type': 'consolidation'}}]
    # return [{'action': 'action', 'source': territories[0].name, 'data': {'type': 'muster'}}]

  def march_move(self, game, player, my_territories):
    return [{'action': 'action', 'source': my_territories[0].name, 'data': {'target': 'todo'}}]





