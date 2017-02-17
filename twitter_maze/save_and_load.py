"""
Interface for saving and loading tweet objects in order to play the
game offline.
"""

import pickle, os

from retrieve_data import TwitterAttributes

pickle_path = os.getcwd() + '/pickled_tweets/'


def save(pickle_path, t_object):
    """
    Saves the current tweet, search, and trend attributes to a file for later retrieval.
    """

    for index, trend in enumerate(t_object[0][0]['trends']):
        print('{}: {}'.format(index, trend['name']))

    print(t_object[1])
    print(t_object[2])

    print("Do you want to pickle the current twitter attributes? ")
    pickle_yn = input("Y/N: ")

    if 'y' in pickle_yn.lower():
        print('Please enter a file name:')
        file_name = input('>>> ')
        with open('{}{}.p'.format(pickle_path, file_name), 'wb') as file:
            try:
                pickle.dump(t_object, file, protocol=pickle.HIGHEST_PROTOCOL)
            except pickle.PicklingError:
                print("There was an error pickling the twitter attributes!")


def load():
    """
    Loads the attributes from a file (trends, tweets, and chosen tweet).
    """

    global pickle_path

    pickles = os.listdir(pickle_path)

    for p in pickles:
        print(p)
    print()

    print("Which Tweets do you want to use?")
    file_name = input('>>> ')

    with open('{}{}.p'.format(pickle_path, file_name), 'rb') as file:
        try:
            unpickled_thingy = pickle.load(file)
            return unpickled_thingy
        except EOFError:
            print("There's nothing there! Please choose a different file.")

t_object = TwitterAttributes()

k = (t_object.trends, t_object.found_tweets, t_object.chosen_tweet)

save(pickle_path, k)

k = load(pickle_path)
