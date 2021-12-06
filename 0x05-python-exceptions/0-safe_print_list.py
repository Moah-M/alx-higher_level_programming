#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end='')
        except:
            break
        else:
            count += 1

    print('')
    return count
