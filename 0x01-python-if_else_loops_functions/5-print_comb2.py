#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(f"{99}")
        break
    print("{02d},".format(i), end=" ")
