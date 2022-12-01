#!/usr/bin/python3
import sys

n = len(sys.argv)
print("{} argument:".format(n))
for x in sys.argv:
    print("{}: {}".format(n, x))
