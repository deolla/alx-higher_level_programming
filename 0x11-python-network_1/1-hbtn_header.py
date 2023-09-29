#!/usr/bin/python3
"""Makes in a URL, sends a request to URL."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        i = response.headers.get('X-Request-Id')
        print(i)
