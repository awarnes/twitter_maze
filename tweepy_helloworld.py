"""
Testing Tweepy API functions
"""


from private import secrets
import tweepy
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

print(search_trend)

top_10_tweets_from_search_trend = api.search(search_trend, count=10, result_type='popular', lang='en')

for tweet in top_10_tweets_from_search_trend:
    print(tweet.text)
    print('-'*len(tweet.text))