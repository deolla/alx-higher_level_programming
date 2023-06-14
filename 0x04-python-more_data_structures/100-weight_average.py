#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_sum = sum(x * y for x, y in my_list)
    total_weight = sum(y for _, y in my_list)
    average_weight = weight_sum / total_weight

    return average_weight
