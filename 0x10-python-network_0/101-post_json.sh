#!/bin/bash
# Sends a JSON POST request to URL passed as first argument & displays the body of response.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
