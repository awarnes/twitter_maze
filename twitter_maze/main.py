""":
    The main game function.
    """


import maze_gen

from retrieve_data import TwitterAttributes

# TODO: Check operating system. Only allow playing on BSD systems.
# TODO: OR change move settings ony


if __name__ == "__main__":

    twitter_attributes = TwitterAttributes()


    maze_gen.print_board(twitter_attributes.chosen_tweet.upper())
