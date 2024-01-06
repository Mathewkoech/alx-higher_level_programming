#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
prints lists of integers in reverse order
"""
    if not my_list:
        return None
    for num in reversed(my_list):
        print("{:d}".format(num))
