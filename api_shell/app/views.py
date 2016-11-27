from flask import Flask, request, render_template
from app import app
import tweepy


class Views:
    consumer_key = "CqLZJckBa8Ph9UxTVEuDbaGXV"
    consumer_secret = "1RCRgjCA2BOPc2ZXhpukZUvLt03mBGDuq5RrgUNmLYxqatkjYu"
    access_token = "4097923872-9pPhoqnzB6Ldixx8tsm6kxHMUyLefmnetFGmKp0"
    access_token_secret = "NVSy5u6v8pKmMY9MvAptcqoh7OeQt85EuafsYydUxjfH1"


    # configure Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    @app.route('/search/<input>')
    def main(input):
        global api
        class MyStreamListener(tweepy.StreamListener):
            def on_status(self, status):
                this_status = status
                # print(this_status.user.screen_name)
                print [this_status.text, this_status.user.screen_name, this_status.user.profile_image_url_https]
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        tag = u'Fidel'

        myStream.filter(track=[tag], async=True)
