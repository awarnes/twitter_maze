"""
Trying out making the whole return a single class that can help with storage,
retrieval and scrubbing in one importable place.
"""


import (tweepy, pickle)
from random import (randint, choice)
from re import (scrub)

from private import secrets


class Tweet:

    CONSUMER_KEY = secrets.CONSUMER_KEY
    CONSUMER_SECRET = secrets.CONSUMER_SECRET
    ACCESS_TOKEN = secrets.ACCESS_TOKEN
    ACCESS_SECRET = secrets.ACCESS_SECRET

    def __init__(self, woeid='23424977', file_path="/Users/alexanderwarnes/Documents/abw_codes/Git/twitter_maze/private/top_10_tweets_data.p"):
        """Accept option of location (default USA) and sets-up the api for other methods."""

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.woeid = woeid

        self.file_path = file_path

        self.trends = None
        self.found_tweets = None
        self.chosen_tweet = None


    def get_trends(self):
        """
        Returns top trends as a trends object from the given woeid (default=USA).
        """

        self.trends = api.trends_place(woeid)

        return None


    def get_popular_tweets(self, amount):
        """
        Returns top tweets as a search object from a randomly selected trend.
        """

        if self.trends == None:
            self.get_trends()

        random_trend = randint(0, len(self.trends[0]['trends']))

        search_trend = self.trends[0]['trends'][random_trend]['name']

        self.found_tweets = api.search(search_trend, count=amount, result_type='popular', lang='en')

        return None


    def tweet_scrubber(self, length):
        """
        Returns the scrubbed text of a random tweet and the tweet object itself separately.
        """

        tweet_texts = list()

        if self.found_tweets == None:
            self.get_popular_tweets()

        for tweet in self.found_tweets:
            text = re.sub(r'( https\:\/\/.*)$','',tweet.text)
            text = re.sub(r'[\n\t]', ' ', text)
            tweet_texts.append(text)


        random_choices = [text for text in tweet_texts if len(text) >= length]

        return choice(random_choices)


    def set_file_path(self):
        """Changes the save/load file for pickling."""

        print("What is the path to the file you need to use?")
        self.file_path = input(">>> ")

        return None


    def pickle(self, pickling_thingy):
        """
        Saves a tweet, search, or trend object to a file for later retrieval.
        """

        print("Do you want to pickle this tweet object? ")
        pickle_yn = input("Y/N: ")

        if 'y' in pickle_yn.lower():

            with open(self.file_path, 'wb') as file:
                try:
                    pickle.dump(pickling_thingy, file, protocol=pickle.HIGHEST_PROTOCOL)
                except pickle.PicklingError:
                    print("There was an error pickling the tweet_objects!")

            return None


    def unpickle(self):
        """
        Loads an object from a file (tweet, search, and trend).
        """

        with open(file_path, 'rb') as file:
            unpickled_thingy = pickle.load(file)

        return unpickled_thingy
