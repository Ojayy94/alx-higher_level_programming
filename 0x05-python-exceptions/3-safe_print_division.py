#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        i = a / b
    except (TypeError, ZeroDivisionError):
        i = None
    finally:
        print("Inside result: {}".format(i))
    return i
