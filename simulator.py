from game import Game
from player import Player
from player import RandomAi, SimpleAi

def run():
  results = {}


  for i in range(0,1000):
    players = [
      Player('martell',   RandomAi('random-martell')),
      Player('baratheon', RandomAi('random-baratheon')),
      Player('tyrell',    RandomAi('random-tyrell')),
      Player('lannister', RandomAi('random-lannister')),
      Player('greyjoy',   RandomAi('random-greyjoy')),
      Player('stark',     RandomAi('random-stark')),
    ]

    game = Game(players)
    winner = game.run()
    wins = results.get(winner.ai.name, 0)
    results[winner.ai.name] = wins + 1



  print str(results)

if __name__ == '__main__':
  run()