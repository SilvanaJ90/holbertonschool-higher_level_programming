#!/usr/bin/python3
def max_integer(my_list=[]):
    large = int(len(my_list))
    for i in my_list:
        if large == 0:
            return None
        elif i > large:
            large = i
    return large
