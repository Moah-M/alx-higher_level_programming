#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    if x == 0:
        new_tuple = (x, None)
    else:
        new_tuple = (x, y)
    return new_tuple
