from names import get_first_name


SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
PRINTED = {rank: f'***{rank}***' for rank in RANKS}

MESSAGES = {
    'ask_start': 'Want to play?(y/n) ',
    'ask_card' : 'Want new card?(y/n) ',
    'dealer_fall': 'Dealer are fall! All players in game are win',
    'eq': '{player} player has {points} points so it equal with dealer points\n {player} bid will be back',
    'win': '{} player are win',
    'lose': '{} player are lose',
    'rerun': 'Want to play again?(y/n)'
}


def random_name():
    return get_first_name(gender="male")


NAMES = [random_name() for _ in range(20)]
