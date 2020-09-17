#!/usr/bin/python3
"""How many subs?
    """
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers

    Args:
        subreddit (str): user the reddit

    Returns:
        int: number of the subscritor
    """
    agent_user = {'User-agent': 'TrickyChart131'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    get_req = requests.get(url, headers=agent_user)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        return (0)
    else:
        return (get_subs["data"]["subscribers"])
