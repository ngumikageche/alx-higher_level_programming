#!/usr/bin/python
"""Defines a func that conv From JSON string to Object"""


import json


def from_json_string(my_str):
    """ func that returns an object represented by a json file
    Args:
        my_str (string): python string
    Returns:
        returns a python object
    """
    return json.loads(my_str)
