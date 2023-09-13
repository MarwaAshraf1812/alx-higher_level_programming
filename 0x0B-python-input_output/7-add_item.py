#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a JSON file
"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        list_item = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list_item = []
    if len(sys.argv) < 1:
        sys.exit()
    list_item.extend(sys.argv[1:])
    save_to_json_file(list_item, "add_item.json")
