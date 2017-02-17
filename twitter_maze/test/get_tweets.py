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


random_trend = randint(0, len(usa_trends[0]['trends']))

search_trend = usa_trends[0]['trends'][random_trend]['name']

print(search_trend)

top_10_tweets_from_search_trend = api.search(search_trend, count=10, result_type='popular', lang='en')

for tweet in top_10_tweets_from_search_trend:
    print(tweet.text)
    print('-'*len(tweet.text))

print("Do you want to pickle this tweet object? ")
pickle_yn = input("Y/N: ")

if 'y' in pickle_yn.lower():

    file_path = os.getcwd() + "/pickled_tweets/"

    with open(file_path, 'wb') as file:
        try:
            pickle.dump(top_10_tweets_from_search_trend, file, protocol=pickle.HIGHEST_PROTOCOL)
        except pickle.PicklingError:
            print("There was an error pickling the tweet objects!")
