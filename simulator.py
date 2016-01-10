from game import Game
from player import Player

def run():
  players = [
    Player(),
    Player(),
    Player(),
    Player(),
    Player(),
    Player(),
  ]

  game = Game(players)
  winner = game.run()
  print winner