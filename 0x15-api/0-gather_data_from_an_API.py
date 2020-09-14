#!/usr/bin/python3
"""gethet data from api
    """
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    url_id_all = "https://jsonplaceholder.typicode.com/\
        todos/?userId=" + USER_ID
    url_id_task = "https://jsonplaceholder.typicode.com/\
        todos/?completed=true&userId=" + USER_ID
    req_user = requests.get(url_user).json()
    req_id_task = requests.get(url_id_task).json()
    req_id_all = requests.get(url_id_all).json()
    EMPLOYEE_NAME = req_user['name']
    NUMBER_OF_DONE_TASKS = len(req_id_task)
    TOTAL_NUMBER_OF_TASKS = len(req_id_all)
    print("Employee {} is done with tasks({}/{}):\
        ".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in req_id_task:
        print("	 {}".format(task.get("title")))
