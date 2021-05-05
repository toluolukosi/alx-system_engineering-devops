#!/usr/bin/python3
"""gathers data from an API"""
import json
import requests
import sys


def getInformation(employeeid):
    """Returns information based on ID"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users').json()
    tasks = requests.get(url + 'todos').json()
    _allData = {}
    for user in users:
        _users = []
        for task in tasks:
            if user['id'] == task['userId']:
                userData = {}
                userData['task'] = task['title']
                userData['completed'] = task['completed']
                userData['username'] = user['username']
                _users.append(userData)
        _allData[user['id']] = _users
    with open('todo_all_employees.json', 'w') as f:
        json.dump(_allData, f)


if __name__ == '__main__':
    getInformation()
