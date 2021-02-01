#!/usr/bin/python3
"""extended Python script to export data in the CSV format."""
if __name__ == "__main__":
    import csv
    from json import dumps
    from requests import get
    from sys import argv

    baseURL = "https://jsonplaceholder.typicode.com/"
    user = get(baseURL + "users/" + argv[1])
    todos = get(baseURL + "todos?userId=" + argv[1])
    name = user.json().get("name")
    hidict = {"{}".format(argv[1]): []}
    for task in todos.json():
        lodict = {"task": "{}".format(task.get("title")),
                  "completed": "{}".format(task.get("completed")),
                  "username": "{}".format(user.json().get("username"))}
        hidict[argv[1]].append(lodict)
    with open('{}.json'.format(argv[1]), mode='w+') as export_json:
        export_json.write(dumps(hidict))
