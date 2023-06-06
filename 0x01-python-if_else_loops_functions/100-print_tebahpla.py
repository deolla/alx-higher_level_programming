#!/usr/bin/python3

for m in range(90, 64, -1):
    n = chr(m)
    if m % 2 == 0:
        n = n.lower()
    print("{}".format(n), end="")
