#!/usr/bin/python3

import requests
from sys import argv

"""Script that returns information about user todo list"""
j = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                 format(argv[1])).json()
user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(argv[1])).json()
completed_tasks = 0
uncompleted_tasks = 0
for elem in j:
    if elem['completed'] is True:
        completed_tasks = completed_tasks + 1
for elem in j:
    if elem['completed'] is False:
        uncompleted_tasks = uncompleted_tasks + 1
print(j)
print()
print("Employee {} is done with tasks ({}/{}):".
      format(user_name['name'], completed_tasks,
             (completed_tasks + uncompleted_tasks)))
for elem in j:
    if elem['completed'] is True:
        print("\t {}".format(elem['title']))
