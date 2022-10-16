#!/usr/bin/python3
""" Class Student """


class Student:
    """ Doc """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_list = {}
        for i in attrs:
            try:
                new_list[i] = self.__dict__[i]
            except:
                pass
            return new_list
