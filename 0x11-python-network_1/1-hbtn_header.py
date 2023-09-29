#!/usr/bin/python3
"""Makes in a URL, sends a request to URL and displays the value of the X-Request-Id variable found in the header of the response."""
import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    i = response.headers.get('X-Request-Id')
    print(i)
