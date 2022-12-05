#!/usr/bin/python3

def no_c(my_string):
    for element in my_string:
        if element == 'c' or element == 'C':
            del element
        return(element)
