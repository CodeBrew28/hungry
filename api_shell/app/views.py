from flask import Flask, request, render_template
from app import app
import wikipedia

import json
import urllib2

from twitter import *

consumer_key = "CqLZJckBa8Ph9UxTVEuDbaGXV"
consumer_secret = "1RCRgjCA2BOPc2ZXhpukZUvLt03mBGDuq5RrgUNmLYxqatkjYu"
access_token = "4097923872-9pPhoqnzB6Ldixx8tsm6kxHMUyLefmnetFGmKp0"
acess_token_secret = "NVSy5u6v8pKmMY9MvAptcqoh7OeQt85EuafsYydUxjfH1"


# configure Twitter API
twitter = Twitter(
            auth=OAuth(access_token, acess_token_secret, consumer_key, consumer_secret)           
           )

@app.route('/search/<input>')
def main(input):

	#search spotify api for tracks
	artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + input + "&type=artist").read()
	artistJson = json.loads(artistResponse)
	uid = artistJson['artists']['items'][0]['id']
	topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/" + uid + "/top-tracks?country=SE").read()

	playlist = "PLAYLIST: "
	topTracksJson = json.loads(topTracks)
	for track in range(len(topTracksJson['tracks'])):
		playlist += topTracksJson['tracks'][track]['album']['name'] + "  "
	

	#search twitter api for related hashtags
	query = "#" + input
	my_tweets = twitter.search.tweets(q=query)
	hashtags = "RELATED HASHTAGS: " 
	for i in range(len(my_tweets['statuses'][0]['entities']['hashtags'])):
		hashtags += my_tweets['statuses'][0]['entities']['hashtags'][i]['text'] + "  "

	wiki_title = "TITLE: " + wikipedia.page(wikipedia.search(input)[0]).title + "  "
	wiki_information = "INFORMATION: " + wikipedia.page(wikipedia.search(input)[0]).content 


	return playlist +  hashtags + wiki_title + wiki_information

	



