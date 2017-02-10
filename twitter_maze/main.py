""":
    The main game function.
"""


import maze_gen

from retrieve_data import TwitterAttributes


if __name__ == "__main__":

    twitter_attributes = TwitterAttributes()


    path, board = maze_gen.run(twitter_attributes.chosen_tweet.upper())
