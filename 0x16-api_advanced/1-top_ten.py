#!/usr/bin/python3
"""Reddit Api module task 0"""


def top_ten(subreddit):
    """Returns number of subscribers in a given subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "Mozilla/5.0"},
                            allow_redirects=False)
    i = 0
    while i < 10:
        try:
            print(response.json()["data"]["children"][i]["data"]["title"])
            i += 1
        except Exception:
            print(None)
            return
