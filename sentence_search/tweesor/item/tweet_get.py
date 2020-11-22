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
    """
    ツイートを検索するメソッド
    """
    try:
        print("searh_word:{}".format(searh_word))
        KEYWORD = searh_word
        headers = {
            'Authorization': 'Bearer {}'.format(BA),
        }

        params = {
            "q": "{} -filter:retweets".format(KEYWORD), 
            "count": 100
        }
        
        tweet_list = []
        for i in range(10):
            responses = requests.get(API_URL, headers=headers, params=params)
            for tweet in responses.json()['statuses']:

                full_text = tweet['full_text']
                id = tweet['id']
                created_at = tweet['created_at']
                location = tweet['user']['location']
                iine_count = tweet['favorite_count']
                retweet_count = tweet['retweet_count']
                tweet_list.append((full_text, id, location, created_at, searh_word, iine_count, retweet_count))
                max_id = int(tweet["id"]) - 1
                params["max_id"] = max_id

        return tweet_list
    except Exception as e:
        print(e)

    


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

