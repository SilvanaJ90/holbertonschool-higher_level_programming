#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        print("{}".format(div))
    except ZeroDivisionError:
        print("None")
    finally:
        print("{}".format(div))
        