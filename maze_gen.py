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

    for i in range(20):
        line = '.' * 20
        board.append(list(line))

    seen = list()

    options = [move_down, move_up, move_left, move_right]
    row = 10
    column = 10
    counter = 0
    path = list()

    while counter < 140:
        travel_length = randint(1, 4)
        direction = choice(options)
        # print(travel_length, direction)
        for i in range(travel_length):
            row, column = direction(row, column)
            # TODO: somewhere in here is where the loop isn't behaving
            if check_move(row, column, seen) == True:
                counter += 1
                path.append((row, column))
                seen.append((row, column))
                # print(row, column)

    for i, t in zip(tweet_list, path):
        row = t[0]
        column = t[1]
        print(i, (row, column))
        board[row][column] = i

    print_grid(board)

    # for row in board:
    #     print(row)


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


def check_move(row, column, seen):
    if -1 < row < 20:
        if -1 < column < 20:
            if (row, column) not in seen:
                return True
    else:
        return False


def print_grid(board):
    print_counts = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
    line_count = 0
    for row in board:
        print(print_counts[line_count], row)
        line_count += 1

scratchpad()