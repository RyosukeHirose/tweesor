import re
import os
import json
import MeCab
import requests


CK = os.environ['ConsumerKey']
CS = os.environ['ConsumerSecret']
AT = os.environ['TwitterAccessToken']
AS = os.environ['TwitterAccessTokenSecret']
BA = os.environ['BearerACCESSTOKEN']

API_URL = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"

CLASS_LABEL = "__label__1"

def tweet_get(searh_word):
    try:
        KEYWORD = searh_word
        headers = {
            'Authorization': 'Bearer {}'.format(BA),
        }
        params = (
            ('q', KEYWORD),
            ('count', '100'),
        )
        responses = requests.get(API_URL, headers=headers, params=params)
        tweet_list = []
        for tweet in responses.json()['statuses']:
            full_text = tweet['full_text']
            id = tweet['id']
            tweet_list.append((full_text, id))
    except Exception as e:
        print(e)

    return tweet_list


if __name__ == '__main__':
    tweet_get()











def main():
    tweets = get_tweet()
    print(tweets)
    # surfaces = get_surfaces(tweets)     #ツイートを分かち書き
    # write_txt(surfaces)                 #ツイートを書き込み

def get_tweet():
    """
    TwitterからKEYWORDに関連するツイートを取得
    """
    params = {'p': KEYWORD, 'count': 100}
    twitter = OAuth1Session(CK, CS, AT, AS)
    print("twitter:{}".format(twitter))
    req = twitter.get(API_URL, params = params)
    print("req:{}".format(req))
    results = []
    if req.status_code == 200:
        # JSONをパース
        tweets = json.load(req.text)
        for tweet in tweets['statuses']:
            results.append(tweet['full_text'])
        return results
    else:
        print ("Error: %d" % req.status_code)

