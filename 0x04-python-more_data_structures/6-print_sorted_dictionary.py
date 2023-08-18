#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicSorted = sorted(a_dictionary.keys())
    for key in dicSorted:
        print("{}:{}".format(key, str(a_dictionary[key])))
