from Deck import Deck
from Game import Game
from pprint import pprint
from const import NAMES

from Player import Bot

if __name__ == '__main__':
    g = Game()
    g.start_game()
    print(g.player.money)

    # print('\n\nDone')
    # #
    # for pl in g.players:
    #     if isinstance(pl, Bot):
    #         print(pl.print_cards())





