#!/usr/bin/python3
"""obtains info from json placeholder api and returns it in json format"""

import json
import requests
import sys


def getInformation(employeeid):
    """Returns information based on ID"""
    url = "https://jsonplaceholder.typicode.com/"
    endpoint = url + 'users/{}'.format(employeeid)
    employee = requests.get(endpoint).json()
    taskendpoint = url + 'TODOs?userId={}'.format(employee.get('id'))
    tasks = requests.get(taskendpoint).json()
    _id = employee['id']
    _allData = []
    for task in tasks:
        data = {}
        data['task'] = task['title']
        data['completed'] = task['completed']
        data['username'] = employee['username']
        _allData.append(data)
    _final = {_id: _allData}
    with open('{}.json'.format(_id), 'w') as f:
        json.dump(_final, f)


if __name__ == '__main__':
    getInformation(sys.argv[1])
