#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """multiplies two matrices
    arguments:
        m_a (list of lists of ints/floats): first matrix
        m_b (list of lists of ints/floats): second matrix
    raises:
        TypeError: when m_a or m_b is not list of lists of integers and floats
        TypeError: when m_a or m_b is empty
        TypeError: when m_a or m_b have different-sized rows
        ValueError: when m_a and m_b cannot be multiplied
    return:
        the multiplication of m_a by m_b, represented by a matrix
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    b_inver = []
    for le in range(len(m_b[0])):
        row_new = []
        for c in range(len(m_b)):
            row_new.append(m_b[c][le])
        b_inver.append(row_new)
    matrix_new = []
    for row in m_a:
        row_new = []
        for col in b_inver:
            res = 0
            for i in range(len(b_inver[0])):
                res += row[i] * col[i]
            row_new.append(res)
        matrix_new.append(row_new)
    return matrix_new
