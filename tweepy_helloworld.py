"""
Testing Tweepy API functions
"""


from private import secrets
import tweepy

auth = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)

auth.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)