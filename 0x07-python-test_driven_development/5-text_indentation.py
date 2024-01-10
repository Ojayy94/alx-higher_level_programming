#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of
   these characters: ., ? and :
   """


def text_indentation(text):
    """text must be a string, otherwise raise a TypeError exception
       with the message text must be a string

       There should be no space at the beginning
       or at the end of each printed line
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    idx = 0
    while idx < len(text) and text[idx] == ' ':
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
