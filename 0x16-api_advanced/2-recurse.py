#!/usr/bin/python3
"""¡Recurre!
    """
import requests


def recurse(subreddit, hot_list=[], v_aft=''):
    """recurse

    Args:
        subreddit (str):  user the reddit
        hot_list (list, optional): the titile
        v_aft (str, optional): web page "aftter".

    Returns:
        list: contain the titles
    """
    agent_user = {'User-agent': 'TrickyChart131'}
    if v_aft is '':
        new_list = hot_list
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        get_req = requests.get(url, headers=agent_user)
        if get_req.status_code == 404:
            return None
        get_subs = get_req.json()
        dict_p = get_subs["data"]["children"]
        j = len(dict_p)
        for i in range(j):
            new_list.append(dict_p[i]["data"]["title"])
        v_aft = get_subs["data"]["after"]
        recurse(subreddit, hot_list=new_list, v_aft=v_aft)
        return new_list
    else:
        new_list = hot_list
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, v_aft)
        get_req = requests.get(url, headers=agent_user)
        if v_aft is None:
            return new_list
        get_subs = get_req.json()
        dict_p = get_subs["data"]["children"]
        j = len(dict_p)
        for i in range(j):
            new_list.append(dict_p[i]["data"]["title"])
        v_aft = get_subs["data"]["after"]
        recurse(subreddit, hot_list=new_list, v_aft=v_aft)
        return new_list
