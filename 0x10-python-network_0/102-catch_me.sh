#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and a respond with a message You got me!
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me" -o /dev/null
