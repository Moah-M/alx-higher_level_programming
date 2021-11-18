#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    s = len(sys.argv) - 1
    if s != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(x, y, add(x, y)))
            sys.exit(0)
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(x, y, sub(x, y)))
            sys.exit(0)
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(x, y, mul(x, y)))
            sys.exit(0)
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(x, y, div(x, y)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
