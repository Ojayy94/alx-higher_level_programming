#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

   for i in range(0, list_length):
        try:
            i = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            i = 0
        except ZeroDivisionError:
            print("division by 0")
            i = 0
        except IndexError:
            print("out of range")
            i = 0
        finally:
            new_list.append(div)
    return (new_list) 
