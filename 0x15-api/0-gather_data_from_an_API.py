#!/usr/bin/python3
"""
    a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    baseURL = "https://jsonplaceholder.typicode.com/"
    user = get(baseURL + "users/" + argv[1])
    todos = get(baseURL + "todos?userId=" + argv[1])
    name = user.json().get("name")
    completed = 0
    tasks = 0
    for task in todos.json():
        if task.get("completed"):
            completed += 1
        tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed,
                                                          tasks))
    for task in todos.json():
        if task.get("completed"):
            print("\t ", end="")
            print(task.get("title"))
