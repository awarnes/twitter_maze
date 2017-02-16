import curses
import game_play
import maze_gen


def main():


    board, path, cboard = new_game()


    prow, pcolumn = 0, 0
    score = 0
    counter = 0

    for coord in path:
        got_it = False
        while not got_it:
            score += 1
            guess = select_move(prow, pcolumn)
            if guess == coord:
                counter += 1
                prow, pcolumn = coord
                got_it=True
                display(prow, pcolumn, board, cboard)
                # print('\nTweet so far: {} \nTries so far: {}'.format(tweet[:counter],  score))
            else:
                curses.beep()
                y, x = stdscr.getmaxyx()
                msg = "Can't move there!"
                stdscr.addstr(28, ((x // 2)-(len(msg)//2)), msg, curses.A_BLINK)
                stdscr.refresh()

    print('You did it! \n\nScore: {} \nBest possible: {} \nTweet: {}'.format(score, len(tweet), tweet))

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
    return result
# def move_handler(key_assign=None, key_dict={ord('t'):4}):
#     """
#     Implements the game logic.
#     """
#
#     if key_assign:
#         key_dict[ord(key_assign[0])] = key_assign[1]
#     else:
#         c = stdscr.getch()
#         if c in (ord('Q'), ord('q')):
#             return False
#         elif c not in key_dict.keys():
#             curses.beep()
#             curses.flash()
#             y, x = stdscr.getmaxyx()
#             msg = "Can't move there!"
#             stdscr.addstr(28, ((x // 2)-(len(msg)//2)), msg)
#             stdscr.refresh()
#             return True
#         else:
#             stdscr.addstr(28, 15, ' '*40)
#             stdscr.refresh()
#             curses.napms(2000)
#             return key_dict[c]()


def display(row, column, board, cboard):
    """
    Updates the displays for score, tweet, and board.
    """

    for index, krow in enumerate(board):
        krow = '  '.join(krow)
        cboard.addstr(1+index, 1, krow)

    cboard.addch(row+1, column+1, board[row][column], curses.color_pair(1))

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


def init_tweet(tweet):
    """initializes the 'tweet' window"""

    ctweet = curses.newwin(4, 85, 29, 2)

    ctweet.addstr(1,1,tweet)
    ctweet.box()
    ctweet.refresh()

def new_game():
    """Starts a new game and initializes the screen."""

    stdscr.clear()
    stdscr.refresh()

    test_tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'.upper()

    board, path = maze_gen.make_board(test_tweet)

    cboard = init_board(board)
    init_score(test_tweet)
    init_moves()
    init_tweet(test_tweet)

    return board, path, cboard

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
