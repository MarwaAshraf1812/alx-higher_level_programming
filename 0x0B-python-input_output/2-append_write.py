#!/usr/bin/python3
"""Contains the  "append_wrtie" function"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and 
    returns the number of characters added
    """
    if filename == "" or text == "":
        return
    with open(filename, mode='a', encoding="UTF8") as f:
        return f.write(text)
