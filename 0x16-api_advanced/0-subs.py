#!/usr/bin/python3
"""Reddit Api module task 0"""


def number_of_subscribers(subreddit):
    """Returns number of subscribers in a given subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Agent"})

    return(sub_info.json()["data"]["subscribers"])
