#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)

    if x == 0:
        x1 = 0
        x2 = 0
    elif x == 1:
        x1 = tuple_a[0]
        x2 = 0
    else:
        x1 = tuple_a[0]
        x2 = tuple_a[1]

    if y == 0:
        y1 = 0
        y2 = 0
    elif y == 1:
        y1 = tuple_b[0]
        y2 = 0
    else:
        y1 = tuple_b[0]
        y2 = tuple_b[1]

    new_tuple = (x1 + y1, x2 + y2)
    return new_tuple
