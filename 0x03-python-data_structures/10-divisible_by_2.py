#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_a = []
    for i in my_list:
        if i % 2 == 0:
            list_a.append(True)
        else:
            list_a.append(False)
    return list_a
