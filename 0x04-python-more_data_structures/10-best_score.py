#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary (dict): Input dictionary.

   Returns:
        str: The key with the biggest integer value, or None
    """
    if a_dictionary is None:
        return None
    value = 0
    key = None

    for k, v in a_dictionary.items():
        if v > value:
            key = k
            value = v
    return key
