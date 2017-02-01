"""
Play around with building the board
"""
from random import choice

tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'


def scratchpad():
    """
    Create a path for the tweet.
    """

    tweet_list = list(tweet)
    board = list()

    for i in range(20):
        line = '#' * 20
        board.append(list(line))

    row = 10
    column = 10
    seen = list()
    options = [move_down, move_up, move_left, move_right]

    for char in tweet_list:
        seen.append((row, column))
        move = choice(options)
        prop_column, prop_row = move(column, row)
        if (prop_column, prop_row) not in seen:
            board[row][column] = char
            column = prop_column
            row = prop_row

    print(seen)

    for row in board:
        print(row)


def move_down(column, row):
    row += 1
    return column, row


def move_up(column, row):
    row -= 1
    return column, row


def move_left(column, row):
    column -= 1
    return column, row


def move_right(column, row):
    column += 1
    return column, row





scratchpad()