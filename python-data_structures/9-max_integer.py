#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    large_int = int(large)
    for i in my_list:
        if len(my_list) == 0:
            return None
        elif i > large_int:
            large_int = i
    return large_int
