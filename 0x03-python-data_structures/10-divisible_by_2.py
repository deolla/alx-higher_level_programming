#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    score = []
    for m in my_list:
        if m % 2 == 0:
            score.append(True)
        else:
            score.append(False)
    return (score)
