"""
Draft of the user interface, with rudimentary display.
"""
import maze_gen
import os


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
    choice = input('Use your keypad to select 2 for down, 8 for up, 4 for left, or 6 for right:  ')

    if choice in moves:
        move = moves[choice]
    else:
        print('That is not a valid move.')
        return None

    result = maze_gen.move(row, column, move)
    return result


def run(tweet):
    """
    Implement game logic.
    Have user select each move, if correct progress through the tweet.
    Increment score counter with each guess.
    With each guess clear the screen, display the score, display the tweet that has been discovered so far.
    """

    board, path = maze_gen.make_board(test_tweet)
    display(board)

    row, column = 0, 0
    score = 0
    counter = 0

    for coord in path:
        got_it = False
        while not got_it:
            score += 1
            guess = select_move(row, column)
            if guess == coord:
                counter += 1
                row, column = coord
                got_it=True
                os.system('clear')    # THIS WON'T WORK ON WINDOWS
                display(board)
                print('\nTweet so far: {} \nTries so far: {}'.format(tweet[:counter],  score))
            else:
                print('Try again. Tries so far: {}'.format(score))

    print('You did it! \n\nScore: {} \nBest possible: {} \nTweet: {}'.format(score, len(tweet), tweet))


test_tweet = 'I write the best tweets. This tweet is one hundred and forty characters long. This is a tremendous tweet. Every other tweet is a loser. Sad.'.upper()
# test_tweet = 'TEST'
run(test_tweet)
