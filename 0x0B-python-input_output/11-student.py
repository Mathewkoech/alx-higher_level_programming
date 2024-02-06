#!/usr/bin/python3
"""Module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved otherwise retrieve all
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()

        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
                return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
