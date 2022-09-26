#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i != 'C' and i != 'c':
            return my_string
        return my_string.replace(i, "")
