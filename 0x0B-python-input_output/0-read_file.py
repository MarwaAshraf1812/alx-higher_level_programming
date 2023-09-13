#!/usr/bin/python3
"""Contains the read_file function"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open("my_file_0.txt", mode='r', encoding='UTF-8') as f:
        print(f.read(), end="")
