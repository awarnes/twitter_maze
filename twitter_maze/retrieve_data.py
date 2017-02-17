"""
Trying out making the whole return a single class that can help with storage,
retrieval and scrubbing in one importable place.
"""

import pickle, re, os
from random import (randint, choice)

import tweepy

from private import secrets


class TwitterAttributes(object):

    CONSUMER_KEY = secrets.CONSUMER_KEY
    CONSUMER_SECRET = secrets.CONSUMER_SECRET
    ACCESS_TOKEN = secrets.ACCESS_TOKEN
    ACCESS_SECRET = secrets.ACCESS_SECRET

    def __init__(self, woeid='23424977', file_path="/pickled_tweets/"):
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
        self.chosen_tweet, self.chosen_tweet_text = self.tweet_scrubber(60)

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

        tweets = list()

        if self.found_tweets == None:
            self.get_popular_tweets()

        for tweet_object in self.found_tweets:
            tweet_text = re.sub(r'( https\:\/\/.*)$', '', tweet_object.text)
            tweet_text = re.sub(r'[\n\t]', ' ', tweet_text)
            tweets.append((tweet_object, tweet_text))


        random_choices = [tweet for tweet in tweets if len(tweet[1]) >= length]

        #  Sometimes there aren't tweets of a given length.
        try:
            return choice(random_choices)
        except IndexError as e:
            print('No tweets of length {} or greater.'.format(length))
            raise e
