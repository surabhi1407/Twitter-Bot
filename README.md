# Twitter-Bot

This Python-Bot, tweets from a set of pre-created tweets stored in a csv file. An extension of this program can be used to retweet, favourite and follow users based on a specific hashtag.
This can be customised as per the needs :)

## Getting Started

Below are the set of requirements that need to be installed inorder to run on the local machine:

### Prerequisites

- Python 3 (I have used python 3.6, not sure if it works on python 2.7)
- Tweepy API 
- Pandas API 
- Putty/Terminal (for running the script as a backgroud process)
- Twitter account for experimenting

### Installing

Once all the requirements are in place. Copy the code folder in your local machine.
Create a tweets.csv file in the code folder, with the list of tweets to be published (sample tweets.csv provided)

Check the python version on your shell:

```
$ python --version
Python 3.6.1
```
Run the bot. 
The logs will be generated in *bot.log* file in the same folder, you can check the updates in the file. 
You can validate using the twitter account also for the checking the new posted tweets.

```
nohup python twitter_bot.py >>bot.log &
```

## Enhancements

- Retweet file can be used to retweet, fav and follow the users and can be run seperately.
- SMTP can be configured to sent an email report statistics from bot.log.
- Watsapp reports can be configured using Selenium and Chromium browser to sent an watsapp message about the stats.

