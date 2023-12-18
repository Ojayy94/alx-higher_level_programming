#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    a = 0

    try:
        for lst in my_list:
            if lst < x:
                print('{}'.format(my_list[lst]), end='')
                lst += 1

        print()
    except TypeError:
        pass
    finally:
        return lst
