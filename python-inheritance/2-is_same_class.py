#!/usr/bin/python3
from inspect import CO_ASYNC_GENERATOR


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False