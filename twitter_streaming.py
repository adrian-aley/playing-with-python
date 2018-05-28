# -*- Python 3.6 -*-

# twitter_streaming.py

# Import package to process data in JSON format.
try:
    import json
except ImportError:
    import simplejson as json

# Import methods from "twitter" library.
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API.
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API.
twitter_stream = TwitterStream(auth=oauth)
twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')

# Basic use: get a sample of the public data following through Twitter.
# iterator = twitter_stream.statuses.sample()

# Advanced use: get a sample of public data from tweets that contain a word/phrase.
iterator = twitter_stream.statuses.filter(track="Data Science", language="en")

# Set it to stop at X amount of tweets or it will continue running.
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Automatically wraps the data returned by Twitter as a TwitterDictResponse object.
    # Convert it back to the JSON format to print/score.
    # Basic printing of each tweet in the stream.
    # print (json.dumps(tweet)) 
    
    # Pretty printing for JSON data.
    print (json.dumps(tweet, indent=4))
       
    if tweet_count <= 0:
        break
    