#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for li in m_a:
        if type(li) is not list:
            raise TypeError("m_a must be a list of lists")
    for li2 in m_b:
        if type(li2) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for am in m_a:
        for amm in am:
            if type(amm) is not int and type(amm) is not float:
                raise TypeError("m_a should contain only integers")
    for bm in m_b:
        for bmm in bm:
            if type(bmm) is not int and type(bmm) is not float:
                raise TypeError("m_b should contain only integers")

    size_a = len(m_a[0])
    for li in m_a:
        if size_a != len(li):
            raise TypeError("each row of m_a must be of the same size")
    size_b = len(m_b[0])
    for li in m_b:
        if size_b != len(li):
            raise TypeError("each row of m_b must be of the same size")

    col_ma = len(m_a[0])
    fil_mb = len(m_b)
    if col_ma != fil_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    num = 0
    array = []
    matrix = []
    for lst1 in range(len(m_a)):
        for lst2 in range(len(m_b[0])):
            for i in range(len(m_b)):
                num += (m_a[lst1][i] * m_b[i][lst2])
            array.append(num)
            num = 0
        matrix.append(array)
        array = []

    return 
