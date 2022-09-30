#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        if b == 0:
            return None
            print("Inside result: None")
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        print("Inside result: {}".format(div))
        return div
  