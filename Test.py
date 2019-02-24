import tweepy
import json

# Specify the account credentials in the following variables:
consumer_key = 'gvracgdHjxGXcGHPlkI9e2ER5'
consumer_secret = 'tslCrlX8fWeaaeyu2l9PkgxrpfAE745qk2R47fEYpNCANwOZ2V'
access_token = '1945189632-v5kQ4eaDu62MYzL2OyF5GV768bwVDkbXrqDXHt4'
access_token_secret = 'D8CYRTDiN9Ot5NISeLIahqAqdzKGeDcXdV8WfS2yLkB9r'


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
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Python'])