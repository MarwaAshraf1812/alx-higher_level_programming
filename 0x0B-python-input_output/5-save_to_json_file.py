#!/usr/bin/python3
"""
Contains the "from_json_string" fundtion
"""
import json


def save_to_json_file(my_obj, filename):
    """returns an object represented by a JSON string"""
    with open(filename, mode='w', encoding="UTF8") as f:
        json.dump(my_obj, f)
