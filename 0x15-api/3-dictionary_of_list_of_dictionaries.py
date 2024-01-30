#!/usr/bin/python3
""" for the given emp_id should 
export data in JSON format.
"""

import json
import requests


if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    Jusers = users.json()

    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    JsTodo = todo.json()

    all_todo = {}

    for user in Jusers:
        tasks = []
        for task in JsTodo:
            if task.get('userId') == user.get('id'):
                tDict_ = {"username": user.get('username'),
                          "task": task.get('title'),
                          "completed": task.get('completed')}
                tasks.append(tDict_)
        all_todo[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todo, f)
