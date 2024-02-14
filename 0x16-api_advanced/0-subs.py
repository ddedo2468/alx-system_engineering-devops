#!/usr/bin/python3
""" get subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Get subs number"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'AyaTarek95'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        subscribers_num = data['data']['subscribers']
        return subscribers_num

    else:
        return 0
