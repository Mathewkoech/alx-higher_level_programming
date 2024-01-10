#!/usr/bin/python3
def uniq_add(my_list=[]):
    # using set() to remove duplicates
    new_list = set(my_list)
    # return sum of unique integers in list
    return sum(new_list)
