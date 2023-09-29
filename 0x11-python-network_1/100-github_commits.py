#!/usr/bin/python3
"""Takes 2 arguments in order to solve this challenge."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1]
        )

    response = requests.get(url)
    i = response.json()
    try:
        for m in range(10):
            print("{}: {}".format(
                i[m].get("sha"),
                i[m].get("commit").get("author").get("name")))
    except IndexError:
        pass
