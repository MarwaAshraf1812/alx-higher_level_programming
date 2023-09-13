#!/usr/bin/python3
"""
Contains the "Save_to_json_file" fundtion
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation
    """
    if filename == "":
        return
    with open(filename, mode='w', encoding="UTF8") as f:
        json.dump(my_obj, f)
