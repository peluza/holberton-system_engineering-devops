#!/usr/bin/python3
"""Top Ten
    """
import requests


def top_ten(subreddit):
    """top_ten

    Args:
        subreddit (str): user the reddit

    Returns:
        str:  prints the titles of the first 10 hot
    """
    agent_user = {'User-agent': 'TrickyChart131'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    get_req = requests.get(url, headers=agent_user)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        print(None)
    else:
        dict_p = get_subs["data"]["children"]
        j = len(dict_p)
        for i in range(j):
            print(dict_p[i]["data"]["title"])
