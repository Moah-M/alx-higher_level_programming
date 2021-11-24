#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0

    n = 0
    m = 0

    for val in my_list:
        n += val[0] * val[1]
        o += val[1]
    return (n / o)
