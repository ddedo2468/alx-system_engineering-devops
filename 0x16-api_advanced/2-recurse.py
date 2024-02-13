#!/usr/bin/python3
"""get top 10 """
import requests


def recurse(subreddit, topPosts=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for cou in result.get("children"):
        topPosts.append(cou.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, topPosts, after, count)
    return topPosts
