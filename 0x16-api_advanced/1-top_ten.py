#!/usr/bin/python3
"""
   a function that queries the Reddit API and
   prints the titles of the first 10 hot posts
"""
from requests import get


def top_ten(subreddit):
    """ boi howdy kill me """
    try:
        request = get(
                      'https://www.reddit.com/r/{}/hot.json?limit=10'
                      .format(subreddit),
                      headers={'User-Agent': 'custom'},
                      allow_redirects=False)
        for thread in request.json().get('data').get('children'):
            print(thread.get('data').get('title'))
    except:
        print('None')
