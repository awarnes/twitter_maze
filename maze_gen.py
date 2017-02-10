"""
Play around with building the board
"""
from random import choice, randint
from char_freq import char_frequency


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


def find_path(tweet):
    """
    Create a path for the tweet.
    """
    options = [move_down, move_up, move_left, move_right]
    row = 0
    column = 0
    counter = 0
    path = list()

    while counter < len(test_tweet):
        if counter < 6:
            travel_length = 1
            direction = choice([move_down, move_right])
        else:
            travel_length = randint(3, 8)
            direction = choice(options)

        for i in range(travel_length):
            test_row, test_column = direction(row, column)

            moves = [o(row, column) for o in options]
            if any([check_move(t[0], t[1], path) for t in moves]):
                if check_move(test_row, test_column, path):
                    row, column = test_row, test_column
                    path.append((row, column))
                    counter += 1
                else:
                    break
            else:
                return find_path(tweet)

    return path


def make_board(tweet):
    """
    Take in the path, print the board with the extra characters filled in.
    """
    tweet_list = list(tweet)
    path = find_path(tweet)
    all_chars = char_frequency('letter_freq.txt', 'punc_freq.txt')

    board = list()
    for i in range(25):
        line = '%' * 25
        board.append(list(line))

    for i, t in zip(tweet_list, path):
        row = t[0]
        column = t[1]
        board[row][column] = i

    for i, row in enumerate(board):
        board[i] = [choice(all_chars) if x is '%' else x for x in row]

    return board


def print_board(tweet):
    board = make_board(tweet)

    for row in board:
        print(' '.join(row))


def run(tweet):
    board = make_board(tweet)
    path = find_path(tweet)

    return path, board


test_tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'.upper()
print_board(test_tweet)
