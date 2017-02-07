"""
Play around with building the board
"""
from random import choice
from random import randint

tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'


def scratchpad():
    """
    Create a path for the tweet.
    """
    tweet_list = list(tweet)
    board = list()

    for i in range(25):
        line = '.' * 25
        board.append(list(line))

    options = [move_down, move_up, move_left, move_right]
    row = 0
    column = 0
    counter = 0
    path = list()

    while counter < 140:
        travel_length = randint(3, 8)
        direction = choice(options)

        for i in range(travel_length):
            test_row, test_column = direction(row, column)

            moves = [o(row, column) for o in options]
            if any([check_move(t[0], t[1], path) for t in moves]):
                # TODO: is there a place in here I could check density and move toward less dense areas?

                if check_move(test_row, test_column, path):
                    row, column = test_row, test_column
                    path.append((row, column))
                    counter += 1
                else:
                    break
            else:
                print('spiral of death')
                return scratchpad()


    for i, t in zip(tweet_list, path):
        row = t[0]
        column = t[1]
        board[row][column] = i

    for row in board:
        print(' '.join(row))


def move_down(row, column):
    row += 1
    return row, column


def move_up(row, column):
    row -= 1
    return row, column


def move_left(row, column):
    column -= 1
    return row, column


def move_right(row, column):
    column += 1
    return row, column


def check_move(row, column, path):
    if -1 < row < 20:
        if -1 < column < 20:
            if (row, column) not in path:
                return True
    else:
        return False



def print_board(path):
    """
    Take in the path, print the board with the extra characters filled in.
    """


scratchpad()
