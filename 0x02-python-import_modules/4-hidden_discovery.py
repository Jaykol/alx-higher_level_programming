#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    for name in dir():
        if name[0:2] == "__":
            continue
        print(name)
