import re
import tweepy
import os
from collections import defaultdict
import sys

def extract_numbers(text):
    # regex to describe whole numbers and decimals (scientific and other notations are not considered)
    regex = '([-+]?\d+(\.\d+)?)'
    # re returns all captured groups, so the encompassing parenthesis are the topmost group,
    # we ignore the lower ones and return the new list
    return [float(x[0]) for x in re.findall(regex, text)]


def update_counter(numbers):
    for number in numbers:
        number_counter[number]+=1


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        update_counter(extract_numbers(status.text))

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

number_counter = defaultdict(lambda:0)

myStreamListener = MyStreamListener()

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
        print "\nThe results:\n"
        print sorted(number_counter.iteritems(), key=lambda key_value: int(key_value[1]), reverse=True)
        print "\nBye :)"
        sys.exit()