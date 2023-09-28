#!/bin/bash
#  Bash script that takes in a URL and displays all HTTP methods the server will accept.
url=$1
curl -s -I -X OPTIONS "$url" | grep "Allow:" | cut -d " " -f 2-
