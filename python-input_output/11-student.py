#!/usr/bin/python3
""" Class Student """


import json


class Student:
    """ Doc """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Doc """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """ replace instance """
        self.__dict__.update(json)
