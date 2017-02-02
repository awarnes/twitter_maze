"""
Testing Tweepy API functions
"""


from private import secrets
import tweepy, pickle
from random import randint


auth = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)

auth.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_SECRET)

api = tweepy.API(auth)

usa_woeid = '23424977'

usa_trends = api.trends_place(usa_woeid)

# for trend in usa_trends[0]['trends']:
#     print(trend['name'])

random_trend = randint(0, len(usa_trends[0]['trends']))

search_trend = usa_trends[0]['trends'][random_trend]['name']

top_10_tweets_from_search_trend = api.search(search_trend, count=3, result_type='popular', lang='en')

#  NEED TO PICKLE THE FILE FOR OFFLINE USE!!!!
#  NEED TO LEARN ABOUT PICKLING!!!!!
