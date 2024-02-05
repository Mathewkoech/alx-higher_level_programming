#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """Returns attributes and methods of and object
        Args:
            obj: object
        Return:
            list: the list of attributes
    """
    return dir(obj)
