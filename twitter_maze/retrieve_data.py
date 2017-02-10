"""
Trying out making the whole return a single class that can help with storage,
retrieval and scrubbing in one importable place.
"""


import tweepy, pickle, re
from random import (randint, choice)

from private import secrets


class TwitterAttributes(object):

    CONSUMER_KEY = secrets.CONSUMER_KEY
    CONSUMER_SECRET = secrets.CONSUMER_SECRET
    ACCESS_TOKEN = secrets.ACCESS_TOKEN
    ACCESS_SECRET = secrets.ACCESS_SECRET

    def __init__(self, woeid='23424977', file_path="/private/top_10_tweets_data.p"):
        """Accept option of location (default USA) and sets-up the api for other methods."""

        auth = tweepy.OAuthHandler(TwitterAttributes.CONSUMER_KEY, TwitterAttributes.CONSUMER_SECRET)
        auth.set_access_token(TwitterAttributes.ACCESS_TOKEN, TwitterAttributes.ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.woeid = woeid

        self.file_path = file_path

        self.trends = None
        self.found_tweets = None

        self.get_trends()
        self.get_popular_tweets(10)
        self.chosen_tweet = self.tweet_scrubber(60)

    def get_trends(self):
        """
        Returns top trends as a trends attribute from the given woeid (default=USA).
        """

        self.trends = self.api.trends_place(self.woeid)

        return self


    def get_popular_tweets(self, amount):
        """
        Returns top tweets as a search attribute from a randomly selected trend.
        """

        if self.trends == None:
            self.get_trends()

        random_trend = randint(0, len(self.trends[0]['trends']))

        search_trend = self.trends[0]['trends'][random_trend]['name']

        self.found_tweets = self.api.search(search_trend, count=amount, result_type='popular', lang='en')

        return self


    def tweet_scrubber(self, length):
        """
        Returns the scrubbed text of a random tweet and the tweet attribute itself separately.
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

        return self


    def pickle(self):
        """
        Saves the current tweet, search, and trend attributes to a file for later retrieval.
        """

        # options = ("Search", "Trends", "Tweet")
        # print("Which type of object are you pickling?")
        # for opt_index, option in enumerate(options, start=1):
        #     print("{}: {}".format(opt_index, option))
        #
        # try:
        #     opt_choice = int(input("Please enter the number: "))
        # except ValueError:
        #     print("Sorry, cannot pickle that!")


        print("Do you want to pickle the current twitter attributes? ")
        pickle_yn = input("Y/N: ")

        if 'y' in pickle_yn.lower():

            with open(self.file_path, 'wb') as file:
                try:
                    pickle.dump(pickling_thingy, file, protocol=pickle.HIGHEST_PROTOCOL)
                except pickle.PicklingError:
                    print("There was an error pickling the twitter attributes!")

            return self


    def unpickle(self):
        """
        Loads the attributes from a file (tweet, search, and trend).
        """

        with open(file_path, 'rb') as file:
            unpickled_thingy = pickle.load(file)

        return unpickled_thingy
