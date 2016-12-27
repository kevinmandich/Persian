from game import Game
from player import Player
import ai
import pdb

def run():
  results = {}

  for i in range(0,1000):
    players = [
      # Player('Random1', ai.RandomAI()),
      # Player('random2', ai.RandomAI()),
      Player('rand3', ai.RandomAI()),
      Player('rand4', ai.RandomAI()),
      # Player('Simple1', ai.SimpleAI()),
      # Player('Simple2', ai.SimpleAI()),
      Player('Simple3', ai.SimpleAI()),
      Player('Simple4', ai.SimpleAI()),
      Player('Simple5', ai.SimpleAI()),
      Player('Simple6', ai.SimpleAI()),
    ]
    if i % 100 == 0:
      print 'Game {}'.format(i)

    game = Game(players)
    winner = game.run()
    wins = results.get(winner.name, 0)
    results[winner.name] = wins + 1



  print str(results)

if __name__ == '__main__':
  run()