#!/usr/bin/python3
"""Reddit Api module task 2"""


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function to return a list containing titles"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "Mozilla/5.0"},
                            params={"after": after},
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    i = 0
    for elem in response.json()["data"]["children"]:
        hot_list = hot_list + [response.json()["data"]
                                              ["children"][i]["data"]["title"]]
        i += 1

    after = response.json()["data"]["after"]
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
