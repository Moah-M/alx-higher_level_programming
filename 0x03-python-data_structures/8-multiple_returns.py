#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    if x == 0:
        return x, "None"
    else:
        return x, y
