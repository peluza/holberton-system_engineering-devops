#!/usr/bin/python3
"""gethet data from api
    """
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
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in req_id_t:
        print("	 {}".format(task.get("title")))
