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
        print(None)
        return
    try:
        res = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), allow_redirects=False,
                           headers={'User-Agent': 'My User Agent 1.0'},
                           params={'limit': 10}).json()
    except JSONDecodeError:
        return print(None)
    top = res.get('data', {}).get('children', [])
    if len(top) > 0 and top[0].get('kind') != 't3':
        print(None)
        return
    # for post in top:
    #     print (post.get('data', {}).get('title', ''))
    return [print(post.get('data', {}).get('title', None)) for post in top]
