#!/usr/bin/python3

def uniq_add(my_list=[]):
    return(filter(lambda x: x+x, my_list))
