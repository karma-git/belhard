from names import get_first_name
import colorama as clr

colorama_colors = {
    'BLACK': clr.Fore.BLACK,
    'RED': clr.Fore.BLACK,
    'GREEN': clr.Fore.GREEN,
    'YELLOW': clr.Fore.YELLOW,
    'BLUE': clr.Fore.BLUE,
    'MAGENTA': clr.Fore.MAGENTA,
    'CYAN': clr.Fore.CYAN,
    'WHITE': clr.Fore.WHITE,
    'LIGHTWHITE_EX': clr.Fore.LIGHTWHITE_EX,
    'LIGHTRED_EX': clr.Fore.LIGHTRED_EX,
    'LIGHTBLUE_EX': clr.Fore.LIGHTBLUE_EX,
    'LIGHTYELLOW_EX': clr.Fore.LIGHTYELLOW_EX,
}


def colored(color, text):
    """
    The method takes color and some str and return colored string.
    """
    global colorama_colors
    colored_text = colorama_colors.get(color.upper()) + str(text) + clr.Style.RESET_ALL
    return colored_text


SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

MESSAGES = {
    # System messages: Yellow / Light_Yellow
    'ask_name': colored('LIGHTYELLOW_EX', 'Hello Stranger, what is your name?: '),
    'ask_bot_count': colored('LIGHTYELLOW_EX', 'Chose a bots count (from 0 to 3): '),
    'ask_start': colored('LIGHTYELLOW_EX', 'Want to play blackjack?(y/n): '),
    'ask_card': colored('LIGHTYELLOW_EX', 'Want to "hit" a card?""(y/n): '),
    'ask_bet': colored('LIGHTYELLOW_EX', 'Make your bet (1-19 $): '),
    'ask_rerun': colored('LIGHTYELLOW_EX', 'Want to play again?(y/n)'),
    # Shuffle
    'initial_deal': colored('yellow', '\n!!! Initial deal !!!\n'),
    'circle_num': colored('yellow', '\n!!! Deal {} !!!\n'),
    'alive_players': colored('yellow', '\nPlayers in the game:\n'),
    'no_players': colored('yellow', '\nThere are no players in game\n'),

    # Dealer
    'dealer_fall': colored('magenta', 'Dealer has just fallen! All remained players in the game won (bet x2)'),
    'eq': colored('magenta', """{player} hand value equal with dealer's. 
                    Bet coast has been returned to player's account. """),
    'dealer_game': colored('magenta', '\nStart Game versus Dealer !!! \n'),

    # Results
    'win': colored('GREEN', '{player} player is win'
                            '\nhand value -> {score} | '
                            'profit -> {profit}$ | '
                            'bank -> {bank}$'),
    'equal': colored('LIGHTWHITE_EX', '{player} players bet has been returned'
                                      '\nhand value -> {score} | '
                                      'bet -> {profit}$ | '
                                      'bank -> {bank}$'),

    'lose': colored('RED', '{player} player is lose'
                           '\nscore -> {score} | '
                           '-money -> {profit}$ | '
                           'bank -> {bank}$'),

}


def random_name():
    """
    Generating a name for bot.
    """
    return get_first_name(gender="male")


NAMES = list({random_name() for _ in range(20)})  # set due to we want to get unique names for bots
