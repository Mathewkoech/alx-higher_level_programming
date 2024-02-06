#!/usr/bin/python3
"""Module for append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after
    each line containing a specific string

    Attributes:
        filename (:obj:`str`, optional): name of the file
        search_string (:obj:`str`, optional): string to look for
        new_string (:obj:`str`, optional): string to append

    """
    line_data = []

    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line_data.append(line)
            if search_string in line:
                line_data.append(new_string)
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(line_data)
