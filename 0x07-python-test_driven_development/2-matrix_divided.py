#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers or floats
       otherwise raise a TypeError exception with the message
       'matrix must be a matrix (list of lists) of integers/floats'

       Each row of the matrix must be of the same size, otherwise raise a
       TypeError exception with the message
       'Each row of the matrix must have the same size'

       div must be a number (integer or float), otherwise raise a
       TypeError exception with the message 'div must be a number'

       div can’t be equal to 0, otherwise raise a
       ZeroDivisionError exception with the message 'division by zero'

       All elements of the matrix should be divided by div
       rounded to 2 decimal places

       Returns a new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    else:
        return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
