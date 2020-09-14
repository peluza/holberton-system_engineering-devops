#!/usr/bin/python3
"""gethet data from api
    """
import json
import requests
import sys

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_id_all = "https://jsonplaceholder.typicode.com/todos/"
    req_user = requests.get(url_user).json()
    req_id_all = requests.get(url_id_all).json()
    FILE = "todo_all_employees.json"
    dict_json_end = {}
    for users in req_user:
        list_json = []
        USER_ID = users.get('id')
        USERNAME = users.get("username")
        for task in req_id_all:
            if task.get("userId") == USER_ID:
                TASK_COMPLETED_STATUS = task.get("completed")
                TASK_TITLE = task.get("title")
                dic = {'task': TASK_TITLE,
                       'completed': TASK_COMPLETED_STATUS, 'username': USERNAME}
                list_json.append(dic)
    dict_json_end = {USER_ID: list_json}
    json_str = json.dumps(dict_json_end)
    with open(FILE, mode="w", encoding='utf-8') as file_json:
        file_json.write(json_str)
