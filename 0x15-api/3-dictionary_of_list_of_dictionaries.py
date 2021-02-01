#!/usr/bin/python3
"""extended Python script to export all data in the json format."""
if __name__ == "__main__":
    import csv
    from json import dumps
    from requests import get

    baseURL = "https://jsonplaceholder.typicode.com/"
    users = get(baseURL + "users")
    jusers = users.json()
    hidict = {}
    for user in jusers:
        userID = user.get("id")
        todos = get(baseURL + "todos?userId=" + str(userID))
        hidict[userID] = []
        for task in todos.json():
            lodict = {"task": "{}".format(task.get("title")),
                      "completed": task.get("completed"),
                      "username": "{}".format(user.get("username"))}
            hidict[userID].append(lodict)
    with open('todo_all_employees.json', mode='w+') as export_json:
        export_json.write(dumps(hidict))
