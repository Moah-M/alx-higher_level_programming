#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    new_str = []
    for x in my_string:
        if x == "c" or x == "C":
            continue
        else:
            new_str.append(x)
    for m in new_str:
        new_string = new_string + m
    return new_string
