#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            for j in my_list:
                if j > i:
                    return j
                else:
                    continue
    return j
