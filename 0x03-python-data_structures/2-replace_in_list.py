#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for element in my_list:
        if idx < 0:
            return my_list
        elif idx > len(element):
            return my_list

