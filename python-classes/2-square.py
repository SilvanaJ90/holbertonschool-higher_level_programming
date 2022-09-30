#!/usr/bin/python3
""" Class Square """

class Square:
    """ create Square size private"""
    try:
        def __init__(self, size=0):
            self.__size = size
    
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")