#!/usr/bin/python3
"""Takes in a URL and an email address."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)
    html = response.text
    print(html)
