#!/usr/bin/python3
"""
Contains the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" """
    if filename == "":
        return
    with open(filename, mode='w', encoding="UTF8") as file_name:
        json.load(file_name)
