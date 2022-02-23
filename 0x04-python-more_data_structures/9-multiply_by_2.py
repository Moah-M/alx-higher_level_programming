#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for val in new.keys():
        new[val] *= 2
    return new
