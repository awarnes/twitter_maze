from private.top_10_tweets_data import top_10_tweets_test
import tweepy


for tweet in top_10_tweets_test:
    print(tweet.text)
    print('-'*len(tweet.text))