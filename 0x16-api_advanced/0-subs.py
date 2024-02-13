#!/usr/bin/python3
"""get subs"""
import requests


def number_of_subscribers(subreddit):
    """get the number of reddit subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 404:
        return 0
    result = res.json().get("data")
    return result.get("subscribers")
