#!/usr/bin/python3
"""
get data from api for the given
emp id the script should get the name
and the completed task
"""

import requests
import sys
import csv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]

    emp_todo = requests.get(f"{url}users/{sys.argv[1]}/todos")
    emp_name = requests.get(f"{url}users/{sys.argv[1]}")

    emp_todo = emp_todo.json()
    emp_name = emp_name.json()['username']

    done_tasks = 0

    for task in emp_todo:
        if task['completed']:
            done_tasks += 1

    csvFileName = id + ".csv"

    with open(csvFileName, 'w', newline='') as file:
        fileWriting = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for line in emp_todo:
            fileWriting.writerow([id, emp_name,
                                  line.get('completed'), line.get('title')])
