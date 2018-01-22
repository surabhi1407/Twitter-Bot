

## V2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:22:35 2018

@author: surabhi
"""

# Import our Twitter credentials from credentials.py
from credentials import *
import pandas as p
import tweepy
from time import sleep

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Read the file 
data = p.read_csv("tweets.csv")
all_tweets=data["tweets"].tolist()



for line in all_tweets:
    try:
       if line =="" or len(line) > 280:
         print("****"*10)
         print(all_tweets.index(line))
         print("pass ",len(line))  
         pass
       else :
         print("****"*10)
         print(all_tweets.index(line))
         print(line)
         api.update_status(line)
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(30)
