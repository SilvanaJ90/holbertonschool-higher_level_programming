#!/usr/bin/python3
"""
class base
"""

from tkinter.messagebox import NO


__nb_objects = 0


class Base:
    """ Doc """
    def __init__(self, id=None):
        if id is not None:
            self.id = None
        else:
            __nb_objects += 1
            self.id = __nb_objects
