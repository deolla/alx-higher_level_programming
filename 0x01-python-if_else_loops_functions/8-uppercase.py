#!/usr/bin/python3

def uppercase(str):
    output = ""
    for m in str:
        if 97 <= ord(m) <= 122:
            output += chr(ord(m) - 32)
        else:
            output += m
    print("{}".format(output))
