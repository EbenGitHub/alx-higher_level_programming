#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed_numbers = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
            printed_numbers += 1
    except (IndexError, TypeError, NameError):
        pass
    print()
    return printed_numbers
