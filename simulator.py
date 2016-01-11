from game import Game
from player import Player

def run():
  players = [
    Player(name='Kevin'),
    Player(name='Will'),
    Player(name='Scot'),
    Player(name='Vidur'),
    Player(name='Andrew'),
    Player(name='Paul'),
  ]

  game = Game(players)
  winner = game.run()
  print winner