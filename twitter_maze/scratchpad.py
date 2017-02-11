"""
Scratchpad for the user interface.
"""
import maze_gen

test_tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'.upper()


def display(board):
    """
    Print the new board after each turn.
    """

    for line in board:
        line = '  '.join(line)
        print(line)


def select_move(row, column):
    """
    Ask the user for the next selection, return new coordinates.
    """

    moves = {'2': 'down', '4': 'left', '6': 'right', '8': 'up'}
    choice = input('Use your keypad to select 2 for down, 8 for up, 4 for left, or 6 for right')

    if choice in moves:
        move = moves[choice]
    else:
        print('That is not a valid move. Try again.')
        return None
        #  TODO: how do I sent this back to the top of this block? recursion ?

    result = maze_gen.move(row, column, move)
    return result


def run(tweet):
    """
    Implement
    """

    path, board = maze_gen.run(test_tweet)
    display(board)
    #
    # row, column = 0, 0

    for coord in path:
        print(coord)
        # TODO: HOLY COW ROW AND COLUMN AND BACKWARDS WHAT THE HECK
        # guess = select_move(row, column)
        # print(guess)
        # print(coord)
        #
        # if guess == coord:
        #     row, column = coord
        #     print('got it!')
        #
        #     print(coord)
        #
        # else:
        #     print('try again')

    display()




    # print(path, board)



run(test_tweet)
# display()
# select_move(0, 1)