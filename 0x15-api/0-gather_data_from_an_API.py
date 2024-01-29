#!/usr/bin/python3
""" get data from api """

import requests
import sys

url = "https://jsonplaceholder.typicode.com/"


emp_todo = requests.get(f"{url}users/{sys.argv[1]}/todos")
emp_name = requests.get(f"{url}users/{sys.argv[1]}")


emp_todo = emp_todo.json()
emp_name = emp_name.json()['name']

total_tasks = 0

for task in emp_todo:
    if task['completed']:
        total_tasks += 1

print(f"Employee {emp_name} is done with tasks({total_tasks}/{len(emp_todo)})")

for line in emp_todo:
    if line['completed']:
        print(f"\t{line['title']}")
