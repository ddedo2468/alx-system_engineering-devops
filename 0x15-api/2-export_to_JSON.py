#!/usr/bin/python3
"""
get data from api for the given
emp id the script should get the name
and the completed task
"""
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]

    emp_todo = requests.get(f"{url}users/{sys.argv[1]}/todos")
    emp_name = requests.get(f"{url}users/{sys.argv[1]}")

    emp_todo = emp_todo.json()
    emp_user_name = emp_name.json()['username']

    totalTasks = []
    updatedUser = {}

    for tasks in emp_todo:
        totalTasks.append(
            {
                "task": tasks.get('title'),
                "completed": tasks.get('completed'),
                "username": emp_user_name,
            })

    updatedUser[id] = totalTasks

    jsonFile = id + ".json"
    with open(jsonFile, 'w') as f:
        json.dump(updatedUser, f)
