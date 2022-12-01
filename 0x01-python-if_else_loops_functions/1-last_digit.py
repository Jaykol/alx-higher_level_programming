#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] > 5:
    print(F"Last digit of {number} is greater than 5")
elif number[-1] == 0:
    print(F"Last digit of {number} is 0")
else:
   print(F"Last digit of {number} is less than 6 and not 0")
