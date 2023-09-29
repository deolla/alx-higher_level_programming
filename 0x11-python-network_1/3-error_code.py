#!/usr/bin/python3
"""Takes in a URL, sends request to URL & displays body of response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys


url = sys.arg[0]

try:
    with urllib.request.urlopen(url) as reponse:
        html = response.read()
        print(html)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
