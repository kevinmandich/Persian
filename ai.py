from fixed import *
from random import shuffle, choice

__all__ = ['RandomAI','SimpleAI', 'HumanAI']

'''
AI methods which need implementation:

reconcile_supply_limit
bid_on_influence
determine_bid_tie_order
'''

class AiPlayer(object):
  def planning_moves(self, game, player):
    my_territories = game.map.territories_for(player, planning=True)
    plan_moves = []
    order_tokens = list(player.order_tokens)
    for t in my_territories:
      if len(order_tokens) > 0:
        for order in order_tokens:
          plan_moves.append({'action': 'planning', 'source': t.name, 'data': {'order': order}})
    return plan_moves

  def bid_options(self, player):
    bids = list(range(0, player.power_tokens+1))
    return bids

  def action_move(self, game, player, action_phase):
    territories_for_move = game.map.territories_for(player, action_phase=action_phase)

    if action_phase == 'Raid':
      plan_moves = self.raid_move(game, player, territories_for_move)
    elif action_phase == 'March':
      plan_moves = self.march_move(game, player, territories_for_move)
    elif action_phase == 'Consolidate':
      plan_moves = self.consolidate_move(game, player, territories_for_move)

    return plan_moves

  def possible_raids(self, game, player, my_territories):
    neighbors = []

    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.order_token and neighbor.owner != player.house:
          neighbors.append({'neighbor': n, 'source': t.name})

    results = []
    if len(neighbors) > 0:
      for plan in neighbors:
        results.append({'action': 'Raid', 'source': plan['source'], 'data': {'target': plan['neighbor']}})
    else:
      results.append({'action': 'Raid', 'source': my_territories[0].name, 'data': {'target': ''}})
    return results

  def possible_consolidate(self, game, player, my_territories):
    results = []
    for t in my_territories:
      results.append({'action': 'Consolidate', 'source': t.name, 'data': {'type': 'consolidation'}})
      results.append({'action': 'Consolidate', 'source': t.name, 'data': {'type': 'muster'}})
    return results

  def possible_march(self, game, player, my_territories):
    results = []
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if neighbor.owner != player.name:
          results.append({'action': 'March', 'source': t.name, 'data': {'target': neighbor.name}})

    if len(results) < 1:
      results.append({'action': 'March', 'source': my_territories[0].name, 'data': {'target': ''}})
    return results

  def possible_muster_territories(self, game, player):
    my_territories = game.map.territories_for(player)
    return filter(lambda x: x.castles > 0, my_territories)

  def possible_muster_for_territory(self, game, player, territory):
    results = []
    # TODO add ship options
    results.append({'action': 'Muster', 'source': territory.name, 'data': { 'units': [{'type': 'new', 'unit_name': 'footmen'}]}})
    results.append({'action': 'Muster', 'source': territory.name, 'data': { 'units': [{'type': 'new', 'unit_name': 'knight'}]}})
    results.append({'action': 'Muster', 'source': territory.name, 'data': { 'units': [{'type': 'new', 'unit_name': 'siege'}]}})
    results.append({'action': 'Muster', 'source': territory.name, 'data': { 'units': [{'type': 'upgrade', 'unit_name': 'knight'}]}})
    results.append({'action': 'Muster', 'source': territory.name, 'data': { 'units': [{'type': 'upgrade', 'unit_name': 'siege'}]}})
    return results


class HumanAI(AiPlayer):
  def planning_move(self, game, player):
    print game
    plans = self.planning_moves(game, player)

    if len(plans) > 0:
      for i, plan in enumerate(plans):
        print "{}: {}".format(i, plan)

      i_input = raw_input("Input comma delimited moves: ")
      order = i_input.split(",")
      result = []
      for i in order:
        result.append(plans[int(i)])
      return result
    else:
      return []

  def bid_on_influence(self, game, influence, player):
    print game
    print ", ".join(["{}-{}: {}".format(p.house, p.name, p.power_tokens) for p in game.players])
    i_input = raw_input("Input power to bid on {} (0 - {}): ".format(influence, player.power_tokens))
    return int(i_input)

  def determine_bid_tie_order(self, game, tying_houses):
    for i, house in enumerate(tying_houses):
      print "{}: {}".format(i, house)

    i_input = raw_input("Input comma delimited house order: ")
    order = i_input.split(",")
    result = []
    for i in order:
      result.append(tying_houses[int(i)])
    return result

  def raid_move(self, game, player, my_territories):
    raids = self.possible_raids(game, player, my_territories)

    for i, raid in enumerate(raids):
      print "{}: {}".format(i, raid)

    i_input = raw_input("Input raid: ")
    return [raids[int(i_input)]]

  def consolidate_move(self, game, player, my_territories):
    consolidates = self.possible_consolidate(game, player, my_territories)
    for i, c in enumerate(consolidates):
      print "{}: {}".format(i, c)

    i_input = raw_input("Input consolidate: ")
    return [consolidates[int(i_input)]]

  def march_move(self, game, player, my_territories):
    marches = self.possible_march(game, player, my_territories)
    for i, m in enumerate(marches):
      print "{}: {}".format(i, m)

    i_input = raw_input("Input march: ")
    return [marches[int(i_input)]]


class RandomAI(AiPlayer):

  def planning_move(self, game, player):
    my_plans = self.planning_moves(game, player)
    if len(my_plans) > 0:
      shuffle(my_plans)
      return [my_plans.pop()]
    else:
      return []

  def raid_move(self, game, player, my_territories):
    neighbors = []
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        neighbors.append({'neighbor': n, 'source': t.name})

    shuffle(neighbors)
    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'Raid', 'source': plan['source'], 'data': {'target': plan['neighbor']}}]
    else:
      return [{'action': 'Raid', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def consolidate_move(self, game, player, my_territories):
    shuffle(my_territories)
    return [{'action': 'Consolidate', 'source': my_territories[0].name, 'data': {'type': 'consolidation'}}]
    # return [{'action': 'action', 'source': territories[0].name, 'data': {'type': 'muster'}}]

  def march_move(self, game, player, my_territories):
    neighbors = []

    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        neighbors.append({'source': t.name, 'name': neighbor.name})

    shuffle(neighbors)
    if len(neighbors) > 0:
      return [{'action': 'March', 'source': neighbors[0]['source'], 'data': {'target': neighbors[0]['name']}}]
    else:
      return [{'action': 'March', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def bid_on_influence(self, game, influence, player):
    options = self.bid_options(player)
    return choice(options)

  def determine_bid_tie_order(self, game, tying_houses):
    shuffle(tying_houses)
    return tying_houses

  def muster(self, game, player):
    return []

class SimpleAI(AiPlayer):
  def reconcile_supply_limit(self, game):
    return [2]

  def muster(self, game, player):
    muster_terrs = self.possible_muster_territories(game, player)
    results = []
    for t in muster_terrs:
      musters = self.possible_muster_for_territory(game, player, t)
      results.append(choice(musters))
    return results

  def bid_on_influence(self, game, influence, player):
    options = self.bid_options(player)
    return choice(options[0:2])

  def determine_bid_tie_order(self, game, tying_houses):
    def cmp_it(x,y):
      if x == self.player.house:
        return -1
      else:
        return x < y
    tying_houses.sort(cmp_it)
    return tying_houses

  def planning_move(self, game, player):
    my_plans = self.planning_moves(game, player)
    shuffle(my_plans)
    if len(my_plans) > 0:
      return my_plans
    else:
      return []

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
        if neighbor.order_token and neighbor.owner != player.house:
          neighbors.append({'neighbor': n, 'source': t.name})

    shuffle(neighbors)
    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'Raid', 'source': plan['source'], 'data': {'target': plan['neighbor']}}]
    else:
      return [{'action': 'Raid', 'source': my_territories[0].name, 'data': {'target': ''}}]


  def consolidate_move(self, game, player, my_territories):
    shuffle(my_territories)
    return [{'action': 'Consolidate', 'source': my_territories[0].name, 'data': {'type': 'consolidation'}}]
    # return [{'action': 'action', 'source': territories[0].name, 'data': {'type': 'muster'}}]

  def march_move(self, game, player, my_territories):
    neighbors = []
    for t in my_territories:
      for n in t.neighbors:
        neighbor = game.map.territories[n]
        if ((t.attack_power() > neighbor.defense_power() or neighbor.castles > 0) and neighbor.owner != player.house):
          token = False
          if t.castles > 0 or player.power_tokens > 5:
            token = True
          neighbors.append({'neighbor': n, 'source': t.name, 'token':token})

    shuffle(neighbors)
    if len(neighbors) > 0:
      plan = neighbors.pop()
      return [{'action': 'March', 'source': plan['source'], 'data': {'target': plan['neighbor'], 'leave_token': plan['token']}}]
    else:
      return [{'action': 'March', 'source': my_territories[0].name, 'data': {'target': ''}}]
