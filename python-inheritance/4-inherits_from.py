#!/usr/bin/python3
""" Doc """


def inherits_from(obj, a_class):
    """ if the object is an instance of a class that inherited"""
    if issubclass(a_class, object):
        return True
    if issubclass(obj, object):
        return True
    else:
        return False