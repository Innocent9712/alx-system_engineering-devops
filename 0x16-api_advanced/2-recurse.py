#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""
from json import JSONDecodeError
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Function to get the top 10 post in the subreddit"""
    if type(subreddit) is not str or subreddit is None:
        print()
        return
    if after is None:
        return hot_list
    try:
        res = requests.get(
            "https://www.reddit.com/r/{}/top.json?limit=10&after={}"
            .format(subreddit, after), allow_redirects=False,
            headers={'User-Agent': 'My User Agent 1.0'}).json()
    except JSONDecodeError:
        return None
    top = res.get('data', {}).get('children', None)
    new_titles = []
    if top is not None:
        for post in top:
            title = post.get('data', {}).get('title', None)
            if title is not None:
                new_titles.append(title)
    new_after = res.get('data', {}).get('after', None)
    hot_list += new_titles
    return recurse(subreddit, hot_list, new_after)
