#!/usr/bin/python3

def fizzbuzz():
    value = ""
    for value in range(1, 101):
        if value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        elif value % 3 == 0 and value % 5 == 0:
            print ("FizzBuzz")

        print("")
