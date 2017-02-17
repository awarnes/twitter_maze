"""
Fully playable game run in a terminal.
Because it was made with Curses, this will only run in a BSD environment.
"""
#  Standard Library
import curses
import socket

#  Module Imports
import game_play
import maze_gen
from retrieve_data import TwitterAttributes


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)

    Used to ensure internet connection for getting tweet information from Twitter.

    From User: 7h3rAm
    Answer On: Oct 14 '15
    On Post: http://stackoverflow.com/questions/3764291/checking-network-connection
    """

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        return False

def main():

    board, path, cboard, tweet, cscore, ctweet = new_game()

    #  Where the player is in the path.
    row, column = 0, 0
    #  Where the player needs to be displayed on the board.
    prow, pcolumn = 0, 0
    score = 0
    counter = 0

    for coord in path:
        got_it = False
        while not got_it:
            score += 1
            guess, move = select_move(row, column)
            if guess == coord:
                if move == 'left':
                    pcolumn -= 3
                elif move == 'right':
                    pcolumn += 3
                counter += 1
                row, column = coord
                prow = row
                move
                got_it=True
            else:
                curses.beep()
                y, x = stdscr.getmaxyx()
                msg = "Can't move there!"
                stdscr.addstr(28, ((x // 2)-(len(msg)//2)), msg, curses.A_BLINK)
                stdscr.refresh()
            display(row, column, prow, pcolumn, board, cboard, score, cscore, tweet, counter, ctweet)

    won_game(score, tweet)


def select_move(row, column):
    """
    Ask the user for the next selection, return new coordinates.
    """

    moves = {ord('2'): 'down', ord('4'): 'left', ord('6'): 'right', ord('8'): 'up',
             curses.KEY_DOWN: 'down', curses.KEY_LEFT: 'left', curses.KEY_RIGHT: 'right', curses.KEY_UP: 'up'}
    # choice = input('Use your keypad to select 2 for down, 8 for up, 4 for left, or 6 for right:  ')

    choice = stdscr.getch()

    if choice in moves:
        move = moves[choice]
        stdscr.addstr(28, 15, ' '*40)
        stdscr.refresh()
    else:
        msg = "That's not a valid move!"
        stdscr.addstr(28, ((x // 2)-(len(msg)//2)), msg)
        return None

    result = maze_gen.move(row, column, move)
    return result, move


def won_game(score, tweet):
    """
    The win screen!
    """
    stdscr.clear()
    stdscr.refresh()
    welcome_messages = [
    "Congratulations!", 'You won!', "", "Final Score:", "{}/{}".format(score, len(tweet)), "",
    "1: New Game", "2: Quit"]

    y, x = stdscr.getmaxyx()

    curses.curs_set(0)

    for index, msg in enumerate(welcome_messages):
        stdscr.addstr((y // 2) - (9 - index), ((x // 2)-(len(msg)//2)), msg)

    leave = False

    stdscr.refresh()
    while not leave:
        k = stdscr.getch()
        if k in (ord('n'), ord('N'), ord('1')):
            leave = True
            main()
        elif k in (ord('q'), ord('Q'), ord('2')):
            leave = True
            exit()


def display(row, column, prow, pcolumn, board, cboard, score, cscore, tweet, counter, ctweet):
    """
    Updates the displays for score, tweet, and board.
    """

    for index, krow in enumerate(board):
        krow = '  '.join(krow)
        cboard.addstr(1+index, 1, krow)

    cboard.addch(prow+1, pcolumn+1, board[row][column], curses.A_REVERSE)

    if score < 100:
        cscore.addstr(3, 1, "0"+str(score))
    else:
        cscore.addstr(3, 1, str(score))

    ctweet.addstr(1,1, tweet[:counter], curses.A_UNDERLINE)


    cscore.refresh()
    ctweet.refresh()
    cboard.refresh()


def front_menu(stdscr):
    """
    Welcome screen and front menu for the game.
    """

    welcome_messages = [
    "Welcome to TwitterMaze!", '', "Created by:", "Danny Burrow", "and", "Alex Warnes", '', "1: Start New Game!",
    "2: Quit"
    ]

    y, x = stdscr.getmaxyx()

    curses.curs_set(0)

    for index, msg in enumerate(welcome_messages):
        stdscr.addstr((y // 2) - (9 - index), ((x // 2)-(len(msg)//2)), msg)

    leave = False

    stdscr.refresh()
    while not leave:
        k = stdscr.getch()
        if k in (ord('n'), ord('N'), ord('1')):
            leave = True
            main()
        elif k in (ord('q'), ord('Q'), ord('2')):
            leave = True
            exit()


def init_moves():
    """
    Initializes the 'moves' window.
    Only happens once per game (no updates needed).
    """

    cmoves = curses.newwin(22, 9, 6, 78)
    cmoves.box()

    cmoves.addstr(1, 2, "Moves", curses.A_UNDERLINE)

    cmoves.addstr(3, 3, "Up", curses.A_BOLD)
    cmoves.addstr(4, 4, "8")

    cmoves.addstr(5, 2, "Down", curses.A_BOLD)
    cmoves.addstr(6, 4, "2")

    cmoves.addstr(7, 2, "Left", curses.A_BOLD)
    cmoves.addstr(8, 4, "4")

    cmoves.addstr(9, 2, "Right", curses.A_BOLD)
    cmoves.addstr(10, 4, "6")

    cmoves.addstr(11, 3, "Or", curses.A_BOLD)
    cmoves.addstr(12, 1, "Arrows")

    cmoves.addstr(14, 2, "New", curses.A_BOLD)
    cmoves.addstr(15, 4, "N")

    cmoves.addstr(16, 1, "Restart", curses.A_BOLD)
    cmoves.addstr(17, 4, "R")

    cmoves.addstr(19, 2, "Quit", curses.A_BOLD)
    cmoves.addstr(20, 4, "Q")


    cmoves.refresh()


def init_board(board):
    """Initializes the 'board' window"""

    cboard = curses.newwin(27, 75, 1, 2)
    cboard.box()

    for index, row in enumerate(board):
        row = '  '.join(row)
        cboard.addstr(1+index, 1, row)

    cboard.addch(1, 1, ' ', curses.A_REVERSE & curses.A_BLINK)

    cboard.refresh()
    return cboard


def init_score(tweet):
    """initializes the 'score' window"""

    cscore = curses.newwin(5, 9, 1, 78)
    cscore.box()

    cscore.addstr(1, 1, "Score:", curses.A_UNDERLINE)

    cscore.addstr(3, 1, "000/")

    if len(tweet) < 100:
        cscore.addstr(3, 5, "0"+str(len(tweet)))
    else:
        cscore.addstr(3, 5, str(len(tweet)))

    cscore.refresh()

    return cscore


def init_tweet(tweet):
    """initializes the 'tweet' window"""

    ctweet = curses.newwin(4, 85, 29, 2)

    ctweet.addstr(1,1," "*len(tweet), curses.A_UNDERLINE)
    ctweet.box()
    ctweet.refresh()

    return ctweet


def new_game():
    """Starts a new game and initializes the screen."""

    stdscr.clear()
    stdscr.refresh()

    # test_tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'.upper()

    if internet():
        twitter_attributes = TwitterAttributes()
        if twitter_attributes.TwitterAttributes.ACCESS_SECRET:
            tweet_text = twitter_attributes.chosen_tweet.upper()
    else:
        twitter_attributes = twitter_attributes.unpickle()

    board, path = maze_gen.make_board(tweet_text)

    cboard = init_board(board)
    cscore = init_score(tweet_text)
    init_moves()
    ctweet = init_tweet(tweet_text)

    return board, path, cboard, tweet_text, cscore, ctweet

#  To set the terminal to the correct size if less than 89x34
print("\x1b[8;34;89t")

stdscr = curses.initscr()

#  To ensure that the terminal resize is actually run...
stdscr.getch()


curses.start_color()
curses.use_default_colors()

curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)


curses.wrapper(front_menu)

# signal.signal(signal.SIGWINCH, sigwinch_handler())
