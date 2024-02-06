#!/usr/bin/python3
""" module to create object from JSON"""

import json


def load_from_json_file(filename):
    """creates object from JSON"""
    with open(filename, 'r', encoding="utf-8")as file:
        data = json.load(file)
        return data
