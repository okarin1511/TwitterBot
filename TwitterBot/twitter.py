import tweepy
import time

auth = tweepy.OAuthHandler('*****enter API key here*****','*****enter secret API key*****')

auth.set_access_token('*****enter access token*****','*****enter secret access token*****')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()

search = 'Basketball', 'good'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print (e.reason)
    except StopIteration:
        break