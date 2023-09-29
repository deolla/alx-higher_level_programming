#!/usr/bin/python3
"""Takes in a URL, sends request to URL."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.arg[0]

    try:
        with urllib.request.urlopen(url) as reponse:
            html = response.read()
            print(html)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
