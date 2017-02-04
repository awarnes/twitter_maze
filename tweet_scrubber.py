import tweepy, pickle, re
from random import choice


file_path = "/Users/alexanderwarnes/Documents/abw_codes/Git/twitter_maze/private/top_10_tweets_data.txt"

with open(file_path, 'rb') as file:
    top_10_tweets_data = pickle.load(file)


def tweet_scrubber(data):
    tweet_texts = list()

    for tweet in data:
        text = re.sub(r'( https\:\/\/.*)$','',tweet.text)
        text = re.sub(r'[\n\t]', ' ', text)
        tweet_texts.append(text)


    random_choices = [text for text in tweet_texts if len(text) > 60]

    return choice(random_choices)

print(tweet_scrubber(top_10_tweets_data))