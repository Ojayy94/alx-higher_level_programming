#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary.items())
    for k, v in dict:
        print('{0}: {1}'.format(k, v))
