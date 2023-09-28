#!/bin/bash
# That takes in a URL, sends a request to URL, displays size Of body of the response.
curl -s "$1" | wc -c
