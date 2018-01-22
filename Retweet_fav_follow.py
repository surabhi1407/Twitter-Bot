import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
i=0

# Select the number of tweets you want to retweet

for tweet in tweepy.Cursor(api.search, q='#LifeQuotes').items(10):
    try:
        #Retweet the tweet
        tweet.retweet()
       
       # Favorite the tweet
        tweet.favorite()
        i+=1
        print(i)
        print('Retweeted and favourited the tweet by @' + tweet.user.screen_name)
        print("***"*10)
        sleep(5) 
        #Follow the user 
        if not tweet.user.following:
            tweet.user.follow()
            print("Followed user :" + tweet.user.screen_name )
        else:
            pass
        
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
