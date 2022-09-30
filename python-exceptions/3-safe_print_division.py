#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    else:
        if b == 0:
            return None
    finally:
        print("Inside result: {}".format(div))
        return div
  