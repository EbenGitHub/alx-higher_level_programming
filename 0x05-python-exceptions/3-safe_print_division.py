#!/usr/bin/python3


def safe_print_division(a, b):
    c = None
    try:
        c = a / b
        return c
    except (TypeError, ValueError, ZeroDivisionError):
        pass
        return None
    finally:
        print("Inside result: {}".format(c))
