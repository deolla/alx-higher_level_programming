#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        score = fct(*args)
        return score
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
