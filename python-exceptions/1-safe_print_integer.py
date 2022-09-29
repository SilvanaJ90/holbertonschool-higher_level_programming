#!/usr/bin/python3
def safe_print_integer(value):
    value = 0
    try:
        print("{:d}".format(value),end="")
    except ValueError:
        if not print:
            return False
        else:
            True
