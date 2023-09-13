#!/usr/bin/python3
"""
Contains the "from_json_string" fundtion
"""
import json


def from_json_string(my_obj):
    """returns an object represented by a JSON string"""
    return json.loads(my_obj)
