#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for k, v in a_dictionary:
        new_dict = a_dictionary.copy(k : v*2)
        
    return new_dict
