#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# displays the size of the body of the response.
url="$1"
curl -s "$url" | wc -c
