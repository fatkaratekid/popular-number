import re
import tweepy
import os
from collections import defaultdict
import sys
import logging

logging.basicConfig(level=logging.INFO)

number_counter = defaultdict(lambda:0)


def extract_numbers(text):
    # regex to describe whole numbers and decimals (scientific and other notations are not considered)
    regex = '([-+]?\d+(\.\d+)?)'
    # re returns all captured groups, so the encompassing parenthesis are the topmost group,
    # we ignore the lower ones and return the new list
    return [x[0] for x in re.findall(regex, text)]


def update_counter(numbers):
    for number in numbers:
        number_counter[number]+=1
        

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None, tweet_limit=10):
        self.num_tweets = 0
        self.tweet_limit = int(tweet_limit)
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        update_counter(extract_numbers(status.text))
        self.num_tweets += 1
        logging.debug("total: " + str(self.num_tweets) + " | limit: " + str(self.tweet_limit) + " | condition:" + str(self.num_tweets >= self.tweet_limit))

        if self.num_tweets >= self.tweet_limit:
            logging.info("Retrieved " + str(self.num_tweets) + " tweets from Twitter") 
            self.num_tweets = 0
            return False

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


def get_numbers(tweet_limit=10):
    #tweet_limit - maximal amount of tweets to be retrieved
    logging.info('Tweet limit is ' + str(tweet_limit))

    myStreamListener = MyStreamListener(tweet_limit=tweet_limit)

    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_secret = os.environ['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

    try:
        myStream.sample() #... stream printing out
        #ctrl+c to break

    except KeyboardInterrupt:
        logging.info("Keyboard interrupt detected")
    finally:
        myStream.disconnect()

    logging.debug("The sorted results:")
    logging.debug(sorted(number_counter.iteritems(), key=lambda key_value: int(key_value[1]), reverse=True))
    logging.info("All good! Bye :)")

    return number_counter