#!/usr/bin/python3
"""module for save_to_json_file method"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
    
