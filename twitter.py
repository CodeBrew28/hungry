import tweepy
import urllib


class Queue:
    tail = None
    def __init__(self):
        global tail
        tail = None
    def put(self,d):
        global tail
        node = Node(d, tail)
        tail = node
    def get(self):
        global tail
        current_tail = tail
        tail = current_tail.retrieve()
        return current_tail
    def qsize(self):
        return 0 if tail is None else 1

class Node:
    data = None
    head = None
    def __init__(self,d,h):
        global data
        global head
        data = d
        head = h
    def retrieve(self):
        return head
    def retdata(self):
        return data


tweets = Queue()


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        this_status = status
        #print(this_status.user.screen_name)
        tweets.put([this_status.text, this_status.user.screen_name, this_status.user.profile_image_url_https])
        refresh()


def refresh():
    if tweets.qsize() > 0:
        tweetcontainer = tweets.get()
        tweet = tweetcontainer.retdata()
        tweet[0] = "".join([c for c in tweet[0] if c.isalnum() or c == ' '])
        print('Tweet: {}\nScreen Name: {}\nProfile Pic: {}\n\n'.format(tweet[0], tweet[1], tweet[2]))


consumer_key = "lKVbM5kld0XIchXOKUvWyLz97"
consumer_secret = "rCks6QCEHW2X6rWyQch6j8GDNyUKpXCF5xAfZyM9wyJG6d8p4i"
access_token = "781173939322126336-8rEOCz2gBG3aaswsPzDtxQgVEnM5uNZ"
access_token_secret = "ulLc0vcDyOhOrBUk0gRD3i0cX54wYI9sDIuyHYTHzz55n"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
tag = u'Fidel'

myStream.filter(track=[tag], async=True)