#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        x = len(my_list) - 1
        while x >= 0:
            f = my_list[x]
            print("{:d}".format(f))
            x = x - 1
