#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    html = response.text

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(html)
