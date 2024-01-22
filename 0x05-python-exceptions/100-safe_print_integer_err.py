#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    integer_value = True

    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        integer_value = False
    return integer_value
