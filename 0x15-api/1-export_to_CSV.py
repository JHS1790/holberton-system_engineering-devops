#!/usr/bin/python3
"""extended Python script to export data in the CSV format."""
import csv
from requests import get
from sys import argv

baseURL = "https://jsonplaceholder.typicode.com/"
user = get(baseURL + "users/" + argv[1])
todos = get(baseURL + "todos?userId=" + argv[1])
name = user.json().get("name")
with open('{}.csv'.format(argv[1]), mode='w+') as export_csv:
    task_writer = csv.writer(export_csv,
                             delimiter=',',
                             quotechar='"',
                             quoting=csv.QUOTE_ALL)
    for task in todos.json():
        completed = False
        if task.get("completed"):
            completed = True
        task_writer.writerow([argv[1],
                              name,
                              completed,
                              task.get("title")])
