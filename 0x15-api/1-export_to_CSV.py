#!/usr/bin/python3
"""
Module for educational purpose about API Rest
"""

import requests
from sys import argv

if __name__ == "__main__":
    """Script that returns information about user todo list"""
    j = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                     format(argv[1])).json()
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                             format(argv[1])).json()
    with open('2.csv', mode='a', encoding='utf-8') as csv_file:
        for elem in j:
            a = '"{}","{}","{}","{}"\n'.format(argv[1], user_name['username'],
                                               elem['completed'],
                                               elem['title'])
            csv_file.write(a)
