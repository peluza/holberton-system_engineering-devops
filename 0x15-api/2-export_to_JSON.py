#!/usr/bin/python3
"""gethet data from api
    """
import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    passs = "?completed=true&userId="
    url_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    url_id_a = "https://jsonplaceholder.typicode.com/todos/?userId=" + USER_ID
    url_id_t = "https://jsonplaceholder.typicode.com/todos/" + passs + USER_ID
    req_user = requests.get(url_user).json()
    req_id_t = requests.get(url_id_t).json()
    req_id_a = requests.get(url_id_a).json()
    EMPLOYEE_NAME = req_user['name']
    NUMBER_OF_DONE_TASKS = len(req_id_t)
    TOTAL_NUMBER_OF_TASKS = len(req_id_a)
    USERNAME = req_user.get("username")
    FILE = "{}.json".format(USER_ID)
    list_json = []
    for task in req_id_a:
        TASK_COMPLETED_STATUS = task.get("completed")
        TASK_TITLE = task.get("title")
        dic = {'task': TASK_TITLE,
               'completed': TASK_COMPLETED_STATUS, 'username': USERNAME}
        list_json.append(dic)
    dict_json_id = {USER_ID: list_json}
    json_str = json.dumps(dict_json_id)
    with open(FILE, mode="w", encoding='utf-8') as file_json:
        file_json.write(json_str)
