import tweepy
import json
import webbrowser


# Specify the account credentials in the following variables:
consumer_key = 'gvracgdHjxGXcGHPlkI9e2ER5'
consumer_secret = 'tslCrlX8fWeaaeyu2l9PkgxrpfAE745qk2R47fEYpNCANwOZ2V'
access_token = '1945189632-v5kQ4eaDu62MYzL2OyF5GV768bwVDkbXrqDXHt4'
access_token_secret = 'D8CYRTDiN9Ot5NISeLIahqAqdzKGeDcXdV8WfS2yLkB9r'
file = "results.txt"



# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now analyze your last 50 tweets"!')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
try:
    token = redirect_url = auth.get_authorization_url()
    webbrowser.open(redirect_url, new=2)
except tweepy.TweepError:
    print ('Error! Failed to get request token.')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#API = tweepy.api

pin = input('Verifier:')
auth.get_access_token(pin)
API = tweepy.API(auth)
API.verify_credentials()




# Connect the stream to our listener
print(API.user_timeline())
    
