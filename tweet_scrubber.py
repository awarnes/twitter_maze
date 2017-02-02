import tweepy, pickle, re

file_path = "/Users/alexanderwarnes/Documents/abw_codes/Git/twitter_maze/private/top_10_tweets_data.txt"

with open(file_path, 'rb') as file:
    top_10_tweets_data = pickle.load(file)




for tweet in top_10_tweets_data:
    print("Text:")
    print(re.sub(r'(https\:\/\/.*)$','',tweet.text))
    print()
    print("Tweet ID:")
    print(tweet.id)
    print()
    print("User Info:")
    print("{}, {}".format(tweet.user.name, tweet.user.description))
    print()
    print("Retweet Count:")
    print(tweet.retweet_count)
    print()
    print("Favorite Count:")
    print(tweet.favorite_count)
    # print()
    # print("Full Tweet:")
    # print(tweet)
    print('-'*len(tweet.text))

