#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordli = list(a_dictionary.keys())
    ordli.sort()
    for i in ordli:
        print("{}: {}".format(i, a_dictionary.get(i)))
