import tweepy
import json
import webbrowser
import emoji
import math


# Specify the account credentials in the following variables:
consumer_key = 'gvracgdHjxGXcGHPlkI9e2ER5'
consumer_secret = 'tslCrlX8fWeaaeyu2l9PkgxrpfAE745qk2R47fEYpNCANwOZ2V'
access_token = '1945189632-v5kQ4eaDu62MYzL2OyF5GV768bwVDkbXrqDXHt4'
access_token_secret = 'D8CYRTDiN9Ot5NISeLIahqAqdzKGeDcXdV8WfS2yLkB9r'
file = open("C:/Users/bribr/OneDrive - Washington State University (email.wsu.edu)/Downloads/#TweetYourHeartOut/-TweetYourHeartOut/Program/results2.csv", "wb")



# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


def authWindow(auth):
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        token = redirect_url = auth.get_authorization_url()
        webbrowser.open(redirect_url, new=2)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    return auth

def authenticate_and_scrape(pin, tweetNum, auth):


    print('A')
    auth.get_access_token(pin)
    print(1)
    API = tweepy.API(auth)
    print(2)
    API.verify_credentials()
    print(3)

    print(tweetNum)
    index = 1
    count = tweetNum
    index2 = 1
    c = 0

    for index in range(10):
       # Connect the stream to our listener
       tweets = API.user_timeline(count=200, page=index)
       print(len(tweets))
       for i in tweets:
           temp = emoji.demojize(i.text)
           temp = temp.replace(',', '')
           temp = temp.replace('\n', ' ')
           temp = temp.replace("https", "")
           temp = temp.replace(':', ' ')
           temp = temp + '\n'
           print(c)
           c += 1
           file.write(temp.encode("utf-8"))
           index2 = index2 + 1
           if index2 > count:
               break
       if index2 > count:
           break




#if __name__ == '__main__':
#    listener = PrintListener()
#
#    # Authenticate
#    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#    auth.set_access_token(access_token, access_token_secret)
#try:
#    token = redirect_url = auth.get_authorization_url()
#    webbrowser.open(redirect_url, new=2)
#except tweepy.TweepError:
#    print ('Error! Failed to get request token.')
#
#    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#
##API = tweepy.api
#
#pin = input('Verifier:')
#auth.get_access_token(pin)
#API = tweepy.API(auth)
#API.verify_credentials()
#
#index = 1
#count = int(input("How many Tweets would you like us to analyze:"))
#index2 = 1
#
#
#for index in range(10):
#    # Connect the stream to our listener
#    tweets = API.user_timeline(count=200, page=index)
#    for i in tweets:
#        temp = emoji.demojize(i.text)
#        temp = temp.replace(',', '')
#        temp = temp.replace('\n', ' ')
#        temp = temp.replace("https", "")
#        temp = temp.replace(':', ' ')
#        temp = temp + '\n'
#        file.write(temp.encode("utf-8"))
#        index2 = index2 + 1
#        if index2 > count:
#            break
#    if index2 > count:
#        break
#


    
    
