#!/usr/bin/python3
"""
   a function that queries the Reddit API and
   returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """ reddit is the big gae """
    try:
        request = get('https://www.reddit.com/r/{}/about.json'
                      .format(subreddit),
                      headers={'User-Agent': 'custom'},
                      allow_redirects=False)
        return request.json().get('data').get('subscribers')
    except:
        return 0
