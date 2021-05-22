import tweepy
import time

auth = tweepy.OAuthHandler('*****enter API key here*****','*****enter secret API key*****')

auth.set_access_token('*****enter access token*****','*****enter secret access token*****')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()

hello = "Need sleep."
current_time = "09:52:00"

api.update_status(hello)
print("Tweeted.")

while(hello):
    t = time.localtime()
    tweetTime = time.strftime("%H:%M:%S", t)
    
    if current_time == tweetTime:
        for i in hello:
            api.update_status(i)
            print("Tweeted.")
            time.sleep(60)
        break    
    

print("Done.")

