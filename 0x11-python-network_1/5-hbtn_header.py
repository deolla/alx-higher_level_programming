#!/usr/bin/python3
"""Makes in a URL, sends a request to the URL."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    req_id = response.headers.get('X-Request-Id')
    print(req_id)
