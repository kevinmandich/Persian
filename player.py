from fixed import *

class Player(object):
  '''
  A player object is a player in the game.
  '''

  def __init__(self, name, ai=None):

    self.name             = name
    self.house            = None
    self.order_tokens     = list(ORDER_TOKENS)
    self.ship_units       = 5
    self.footmen_units    = 5
    self.knights_units    = 5
    self.siege_units      = 2
    self.power_tokens     = 5 # start with 5
    self.map_power_tokens = 0

    self.ai               = ai
    self.ai.player        = self

  def __str__(self):
    return 'Player class for player {} playing house {}'.format(self.name, self.house)

  def move(self, game, action_phase=None):
    if game.phase == 'Planning':
      return self.planning_move(game)
    elif game.phase == 'Action':
      return self.action_move(game, action_phase=action_phase)

  def muster(self, game):
    return self.ai.muster(game, self)

  def action_move(self, game, action_phase):
    return self.ai.action_move(game, self, action_phase)

  def planning_move(self, game):
    return self.ai.planning_move(game, self)

  def reconcile_supply_limit(self, game):
    return self.ai.reconcile_supply_limit(game)

  def bid_on_influence(self, game, influence):
    return self.ai.bid_on_influence(game, influence, self)

  def determine_bid_tie_order(self, game, tying_houses):
    return self.ai.determine_bid_tie_order(game, tying_houses)
