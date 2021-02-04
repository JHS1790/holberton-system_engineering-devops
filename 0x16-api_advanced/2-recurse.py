#!/usr/bin/python3
"""
   a recursive function that queries the Reddit API and
   returns a list containing the titles of all hot articles
   for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """ reddit may be bad, but recursion is worse """
    try:
        request = get('https://www.reddit.com/r/{}/hot.json?after={}'.
                      format(subreddit, after),
                      headers={'User-Agent': 'custom'},
                      allow_redirects=False)
        if after is None:
            return hot_list
        for thread in request.json().get('data').get('children'):
            hot_list += [thread.get('data').get('title')]
        after = request.json().get('data').get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
