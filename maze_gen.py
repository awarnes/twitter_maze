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

    # TODO: put all of this in a try

    tweet_list = list(tweet)
    board = list()

    for i in range(20):
        line = '.' * 20
        board.append(list(line))

    options = [move_down, move_up, move_left, move_right]
    row = 10
    column = 10
    counter = 0
    path = list()

    while counter < 140:
        travel_length = randint(1, 4)
        direction = choice(options)
        for i in range(travel_length):
            test_row, test_column = direction(row, column)
            if check_move(test_row, test_column, path):

                row, column = test_row, test_column
                path.append((row, column))
                counter += 1

            else:
                break

    for i, t in zip(tweet_list, path):
        row = t[0]
        column = t[1]
        print(i, (row, column))
        board[row][column] = i


    for row in board:
        print(row)


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
    # row_check = bool(-1 < row < 20)
    # column_check = bool(-1 < column < 20)
    # path_check = bool((row, column) not in path)
    #
    # result = all([row_check, column_check, path_check])
    # return result

    # if -1 < row < 20 and -1 < column < 20 and (row, column) not in path:
    #     return True
    # else:
    #     return False

    if -1 < row < 20:
        if -1 < column < 20:
            if (row, column) not in path:
                return True
    else:
        return False

#     TODO: test all these


scratchpad()