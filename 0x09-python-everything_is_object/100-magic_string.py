#!/usr/bin/python3
def magic_string():
    magic_string.check = getattr(magic_string, 'check', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.check)])
