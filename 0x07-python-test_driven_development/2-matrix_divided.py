#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divide all the elements of a matrix
    arguments:
        matrix (list): list of lists, of integers or floats
        div (int/float): divisor
    raises:
        TypeError: when the matrix contains non numbers
        TypeError: when the matrix contains different sizes rows
        TypeError: when the divisor is not an integer or a float
        ZeroDivisionError: when divisor is 0
    return:
        division result division matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [nmbr for row in matrix for nmbr in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
