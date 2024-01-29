#!/usr/bin/python3

import requests, sys

res = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")

userName = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")

res = res.json()
userName = userName.json()['name']

total_tasks = 0

for task in res:
    if task['completed']:
        total_tasks+=1

print(f"Employee {userName} is done with tasks({total_tasks}/{len(res)})")

for line in res:
    if line['completed']:
        print (f"\t{line['title']}")
