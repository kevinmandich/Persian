from game import Game
from player import Player
from player import RandomAi

def run():
  players = [
    Player('martell', RandomAi()),
    Player('baratheon',  RandomAi()),
    Player('tyrell',  RandomAi()),
    Player('lannister', RandomAi()),
    Player('greyjoy',RandomAi()),
    Player('stark',  RandomAi()),
  ]

  game = Game(players)
  winner = game.run()
  print 'winner is {}'.format(winner)

if __name__ == '__main__':
  run()