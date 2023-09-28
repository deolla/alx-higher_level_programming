#!/bin/bash
# Takes in a URL as argument, sends a GET request to URL & displays body of response
curl -s -H "X-School-User-Id: 98" "$1"
