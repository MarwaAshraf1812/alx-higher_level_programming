#!/usr/bin/python3
"""Contains the read_file function"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as f:
            print(f.read(), end="")
