#!/usr/bin/python3
"""Write a function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
from json import JSONDecodeError
import requests


def number_of_subscribers(subreddit):
    """Function to get the number of subscribers"""
    if type(subreddit) is not str or subreddit is None:
        print()
        return 0
    try:
        res = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), allow_redirects=False,
                           headers={'User-Agent': 'My User Agent 1.0'}).json()
    except JSONDecodeError:
        return 0
    subscribers = res.get('data', {}).get('subscribers', 0)
    return subscribers
