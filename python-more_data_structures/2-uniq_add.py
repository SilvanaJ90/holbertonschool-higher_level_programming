#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in my_list:
        uniq = set(my_list)
        if i <= 0:
            return 0
    return sum(uniq)
