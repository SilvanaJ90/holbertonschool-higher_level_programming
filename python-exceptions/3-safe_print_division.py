#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside resul: None")
    finally:
        print("Inside resul: {}".format(div))
  