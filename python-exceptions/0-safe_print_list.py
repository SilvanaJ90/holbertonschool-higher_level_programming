#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            return x
    except ValueError:
        print("{} is not list".format(x))
