#!/usr/bin/python3
def uppercase(str):
    n = 0
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            n = 32
        else:
            n = 0
        print("{:c}".format(ord(x) - n), end='')
    print()
