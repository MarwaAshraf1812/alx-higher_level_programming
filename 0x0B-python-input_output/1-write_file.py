#!/usr/bin/python3
"""Contains the Write_file function"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    if filename == "" or text == "":
        return
    with open(filename, mode='w', encoding="UTF8") as f:
        return f.write(text)
