#!/bin/bash
# Takes in a URL, sends a POST request to passed URL & displays body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
