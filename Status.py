import tweepy
import requests_oauthlib
import requests
import json

from requests_oauthlib import OAuth1Session

# Specify the account credentials in the following variables:
consumer_key = 'gvracgdHjxGXcGHPlkI9e2ER5'
consumer_secret = 'tslCrlX8fWeaaeyu2l9PkgxrpfAE745qk2R47fEYpNCANwOZ2V'
access_token = '1945189632-v5kQ4eaDu62MYzL2OyF5GV768bwVDkbXrqDXHt4'
access_token_secret = 'D8CYRTDiN9Ot5NISeLIahqAqdzKGeDcXdV8WfS2yLkB9r'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print ("Error! Failed to get request token.")

print(redirect_url)

