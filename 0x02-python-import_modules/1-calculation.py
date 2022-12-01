#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

print("{a} + {b} = {}".format(add(a, b)))
print("{a} - {b} = {}".format(sub(a, b)))
print("{a} / {b} = {}".format(dv(a, b)))
print("{a} * {b} = {}".format(mul(a, b)))

