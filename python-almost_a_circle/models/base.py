#!/usr/bin/python3
"""
class base
"""


class base:
    """ Doc """


    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = None
        else:
            __nb_objects += 1
            self.id = __nb_objects