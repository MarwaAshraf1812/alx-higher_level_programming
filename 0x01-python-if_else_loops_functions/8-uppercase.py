#!/usr/bin/python3
def uppercase(s):
    for char in s:
        char_code = ord(char)
        if ord('a') <= char_code <= ord('z'):
            char_code -= 32
        print(chr(char_code), end="")
    print()
