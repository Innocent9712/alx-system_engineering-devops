#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
to export data in the CSV format.
"""

from fileinput import filename
import requests
from sys import argv

if __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        file_name = "{}.csv".format(argv[1])
    except IndexError:
        exit

    res = requests.get(url)
    res = res.json()
    user_name = "{}".format(res.get('name'))
    res = requests.get(url + "/todos")
    res = res.json()

    for task in res:
        with open(file_name, "a+") as f:
            f.write('"{}","{}","{}","{}"\n'.format(
                                                argv[1],
                                                user_name,
                                                task.get('completed'),
                                                task.get('title')))
