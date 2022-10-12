#!/usr/bin/python3
""" Doc """


def inherits_from(obj, a_class):
    """ if the object is an instance of a class that inherited"""
    if (issubclass(int, a_class)):
        return True
    if (issubclass(object, a_class)):
        return True
    else:
        return False