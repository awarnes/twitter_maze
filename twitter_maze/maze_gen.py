"""
Take in a tweet as a text string, randomly generate a path through the board, then fill in the board
with random characters from an external character set.
"""
from random import choice, randint
from char_freq import char_frequency


def move(row, column, direction):
    moves = {'down': (row + 1, column), 'up': (row - 1, column), 'left': (row, column - 1), 'right': (row, column + 1)}
    result = moves[direction]
    return result


def check_move(row, column, path):
    check_row = -1 < row < 20
    check_column = -1 < column < 20
    check_path = (row, column) not in path

    result = all([check_row, check_column, check_path])
    return result


def find_path(tweet):
    """
    Create a path for the tweet.
    """
    options = ['down', 'up', 'left', 'right']
    row, column = 0, 0
    path = list()

    while len(path) < len(test_tweet):
        if len(path) < 6:
            travel_length = 1
            direction = choice(['down', 'right'])
        else:
            travel_length = randint(3, 8)
            direction = choice(options)

        for _ in range(travel_length):
            test_row, test_column = move(row, column, direction)

            moves = [move(row, column, o) for o in options]
            if any([check_move(t[0], t[1], path) for t in moves]):
                if check_move(test_row, test_column, path):
                    row, column = test_row, test_column
                    path.append((row, column))
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
    all_chars = char_frequency('frequency_tables/letter_freq.txt', 'frequency_tables/punc_freq.txt')
    board = [list(('%'*25)) for _ in range(25)]

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
