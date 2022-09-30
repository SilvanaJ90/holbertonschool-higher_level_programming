#!/usr/bin/python3
from unittest import result


def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        print("Inside result: {}".format(div))
        return div
  