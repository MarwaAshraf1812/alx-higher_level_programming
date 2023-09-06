#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """
        Print a text with two new lines after each '.', '?', and ':' character.

        Args:
        text (str): The input text to be formatted and printed.

        Returns:
        None: This function doesn't return a value; it prints the formatted text directly.
    """
    if not isinstance(text, str) or text is None:
        raise TypeError('text must be a string')

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
