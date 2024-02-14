#!/usr/bin/python3
""" top 10 posts"""

import requests


def top_ten(subreddit):
    """get top 10"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    res = requests.get(url, headers={'User-Agent': 'AyaTarek95'},
                       allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
