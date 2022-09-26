#!/usr/bin/python3
def max_integer(my_list=[]):
    large = len(my_list)
    large_int = int(large)
    for i in my_list:
        if large == 0:
            return None
        elif i > large_int:
            large_int = i
    return large_int
