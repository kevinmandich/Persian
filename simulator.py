from game import Game
from player import Player
from ai import *

def run():
  results = {}

  ai_module = SimpleAI

  for i in range(0,1000):
    players = [
      Player('martell',   ai_module('random-martell')),
      Player('baratheon', ai_module('random-baratheon')),
      Player('tyrell',    ai_module('random-tyrell')),
      Player('lannister', ai_module('random-lannister')),
      Player('greyjoy',   ai_module('random-greyjoy')),
      Player('stark',     ai_module('random-stark')),
    ]
    if i % 100 == 0:
      print 'Game {}'.format(i)

    game = Game(players)
    winner = game.run()
    wins = results.get(winner.ai.name, 0)
    results[winner.ai.name] = wins + 1



  print str(results)

if __name__ == '__main__':
  run()