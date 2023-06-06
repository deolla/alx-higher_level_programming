#!/usr/bin/python3

for m in range(90, 64,- 1):
    print("{:c}".format(m if m % 2 == 0 else m + 32), end='')
