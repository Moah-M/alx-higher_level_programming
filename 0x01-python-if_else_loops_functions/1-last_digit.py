#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
last = "Last digit of"
lesser = "is greater than 6 and not zero"
if last_digit > 5:
    print("{} {} is {} and is greater than 5".format(last, number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} {} is {} and {}".format(last, number, last_digit, lesser))
