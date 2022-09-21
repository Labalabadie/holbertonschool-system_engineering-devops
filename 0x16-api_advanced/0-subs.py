#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Retrives number of subscribers of a subreddit"""
    response = requests.get("https://reddit.com/r/" + subreddit + "/about.json")
	
    return response.data.subscribers
