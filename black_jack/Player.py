import abc
from Deck import Deck
import random
from const import MESSAGES, NAMES
from picture import CardPrinter, CardFromDeck


class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        # self.position = position
        self.bet = 0
        self.full_points = 0
        self.money = 100
        self.name = None

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        print(self, " data")
        self.hand_printer()  # hand printer
        # for card in self.cards: # vs poocheridi
        #     print(card)
        print('Full points: ', self.full_points, '\n')

    def hand_printer(self):
        cards_list = list()
        for card in self.cards:
            card = CardFromDeck(card.suit, card.rank)  # unpack dictionary
            cards_list.append(card)
        else:
            hand_print = CardPrinter.ascii_version_of_card(*cards_list)
            print(hand_print)


class Player(AbstractPlayer):

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if value < max_bet and value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print(f'Your bet is {self.bet}')

    def ask_card(self):
        if self.full_points == 21:
            return False

        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True
        else:
            return False

    def get_name(self, name):
        name = self.name

    def __repr__(self):
        return self.name

class Bot(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = random.choice(NAMES) + '_Bot'

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'give: ', self.bet)

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False

    def __repr__(self):
        name = self.name
        return name


class Dealer(AbstractPlayer):

    max_points = 17

    def change_bet(self, max_bet, min_bet):
        """
        NOTE: This type is Dealer so it has no bets
        """
        raise Exception('This type is dealer so its has no bets')

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False

    def __repr__(self):
        self.name = 'Dealer'
        return self.name