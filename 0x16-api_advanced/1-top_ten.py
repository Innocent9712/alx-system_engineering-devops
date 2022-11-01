#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
from json import JSONDecodeError
import requests


def top_ten(subreddit):
    """Function to get the top 10 post in the subreddit"""
    if type(subreddit) is not str or subreddit is None:
        print()
        return
    try:
        res = requests.get("https://www.reddit.com/r/{}/top.json?limit=10"
                           .format(subreddit), allow_redirects=False,
                           headers={'User-Agent': 'My User Agent 1.0'}).json()
    except JSONDecodeError:
        return print(None)
    top = res.get('data', {}).get('children', [])
    # for post in top:
    #     print (post.get('data', {}).get('title', ''))
    return [print(post.get('data', {}).get('title', '')) for post in top]
