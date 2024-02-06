#!/usr/bin/python3
"""Module for class_to_json method"""


def class_to_json(obj):
    """
    returns the dict desc with simple data
    structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object:
    """
    return obj.__dict__
