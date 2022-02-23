#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    counter = len(sys.argv) - 1

    if counter == 0:
        print("{} arguments.".format(counter))
    elif counter == 1:
        print("{} argument:".format(counter))
    else:
        print("{} arguments:".format(counter))

    if counter >= 1:
        x = 0
        for arg in sys.argv:
            if x != 0:
                print("{}: {}".format(x, arg))
            x += 1
