import tweepy 
from tweepy import OAuthHandler
from key import consumer_key,consumer_secret,access_token,access_token_secret
from tweet_reply import get_quote
import time 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# print (api.me().name)


try:
    api.verify_credentials()
    # print("Authentication Successful")
except:
    print("Authentication Error")

# # user = api.get_user()
# # print(user.screen_name)

# # api.update_status(status='Hello Again - second tweet')
FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = file_read.read().strip()
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')

s=get_quote()
# print(s)


def reply():

    for tweet in reversed(tweets):

        if '#qod' in tweet.full_text.lower():
            
            print(str(tweet.id) + " - "+tweet.full_text)
            api.update_status('@'+tweet.user.screen_name+" Hers's your quote of the day - " +s,tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)

while True:
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
    reply()
    time.sleep(60)        
            
