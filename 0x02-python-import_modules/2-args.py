#!/usr/bin/python3

import sys

args = sys.argv[1:]

count_args = len(args)
plural = 's' if count_args != 1 else ''

print("{} argument{}:".format(count_args, plural))

for m, arg in enumerate(args, start=1):
    print("{}: {}".format(m, arg))
