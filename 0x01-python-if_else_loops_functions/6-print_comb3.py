#!/usr/bin/python3
for number in range(0, 10):
    for nextNumber in range(number + 1, 10):
        if number == 8 and nextNumber == 9:
            print("{}{}".format(number, nextNumber))
        else:
            print("{}{}".format(number, nextNumber), end=", ")
