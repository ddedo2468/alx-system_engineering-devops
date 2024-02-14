#!/usr/bin/python3
""" git reddit subs for a subreddit """
import requests


def number_of_subscribers(subreddit):
    """get the num"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    request = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers)

    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
