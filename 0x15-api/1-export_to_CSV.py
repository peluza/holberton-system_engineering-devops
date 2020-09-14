#!/usr/bin/python3
"""gethet data from api
    """
import csv
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    url_id_all = "https://jsonplaceholder.typicode.com/todos/?userId=" + USER_ID
    url_id_task = "https://jsonplaceholder.typicode.com/todos/?completed=true&userId=" + USER_ID
    req_user = requests.get(url_user).json()
    req_id_task = requests.get(url_id_task).json()
    req_id_all = requests.get(url_id_all).json()
    EMPLOYEE_NAME = req_user['name']
    NUMBER_OF_DONE_TASKS = len(req_id_task)
    TOTAL_NUMBER_OF_TASKS = len(req_id_all)
    USERNAME = req_user.get("username")
    FILE = "{}.csv".format(USER_ID)
    with open(FILE, mode="w", encoding='utf-8') as FILE_CSV:
        for task in req_id_all:
            TASK_COMPLETED_STATUS = task.get("completed")
            TASK_TITLE = task.get("title")
            e_writer = csv.writer(FILE_CSV, delimiter=',',
                                  quotechar='"', quoting=csv.QUOTE_ALL)
            e_writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
