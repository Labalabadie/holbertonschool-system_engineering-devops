#!/usr/bin/python3
"""Reddit Api module task 0"""


def number_of_subscribers(subreddit):
    """Returns number of subscribers in a given subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Mozilla/5.0"})
    try:
        return(response.json()["data"]["subscribers"])
    except Exception:
        return 0
