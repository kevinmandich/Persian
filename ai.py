from fixed import *
from random import shuffle, choice

__all__ = ['RandomAI','SimpleAI']

'''
AI methods which need implementation:

reconcile_supply_limit
bid_on_influence
determine_bid_tie_order
'''

class RandomAI(object):
  def __init__(self, name):
    self.name = name

  def planning_move(self, game, player):
    my_territories = game.map.territories_for(player)
    plan_moves = []
    order_tokens = list(player.order_tokens)
    for t in my_territories:
      shuffle(order_tokens)
      if len(order_tokens) > 0:
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
    #TODO include more source territories to look at
    # for t in my_territories:
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.order_token and neighbor.owner != player.name:
          neighbors.append({'neighbor': n, 'source': t.name})

    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'Raid', 'source': plan['source'], 'data': {'target': plan['neighbor']}}]
    else:
      return [{'action': 'Raid', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def consolidate_move(self, game, player, my_territories):
    return [{'action': 'Consolidate', 'source': my_territories[0].name, 'data': {'type': 'consolidation'}}]
    # return [{'action': 'action', 'source': territories[0].name, 'data': {'type': 'muster'}}]

  def march_move(self, game, player, my_territories):
    neighbors = []
    # for t in my_territories:
    for t in [my_territories[0]]:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.owner != player.name:
          neighbors.append(n)
    if len(neighbors) > 0:
      return [{'action': 'March', 'source': my_territories[0].name, 'data': {'target': neighbors.pop()}}]
    else:
      return [{'action': 'March', 'source': my_territories[0].name, 'data': {'target': ''}}]


class SimpleAI(object):
  def __init__(self, name):
    self.name = name

  def reconcile_supply_limit(self, game):
    return [2]

  def bid_on_influence(self, game, influence):
    a = choice([1,2,3,4])
    return a

  def determine_bid_tie_order(self, game, tying_houses):
    shuffle(tying_houses)
    return tying_houses

  def planning_move(self, game, player):
    my_territories = game.map.territories_for(player)
    plan_moves = []
    order_tokens = list(player.order_tokens)
    for t in my_territories:
      shuffle(order_tokens)
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
    #TODO include more source territories to look at
    # for t in my_territories:
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.order_token and neighbor.owner != player.name:
          neighbors.append({'neighbor': n, 'source': t.name})

    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'Raid', 'source': plan['source'], 'data': {'target': plan['neighbor']}}]
    else:
      return [{'action': 'Raid', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def consolidate_move(self, game, player, my_territories):
    return [{'action': 'Consolidate', 'source': my_territories[0].name, 'data': {'type': 'consolidation'}}]
    # return [{'action': 'action', 'source': territories[0].name, 'data': {'type': 'muster'}}]

  def march_move(self, game, player, my_territories):
    neighbors = []
    # for t in my_territories:
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.castles > 0 and t.knight > neighbor.knight and t.footmen > neighbor.footmen and neighbor.owner != player.name:
          neighbors.append({'neighbor': n, 'source': t.name})

    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'March', 'source': plan['source'], 'data': {'target': plan['neighbor']}}]
    else:
      return [{'action': 'March', 'source': my_territories[0].name, 'data': {'target': ''}}]