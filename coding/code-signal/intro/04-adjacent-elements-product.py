import math


def adjacentElementsProduct(inputArray):
    """
    Return the pair of adjacent elements with the largest product.

    Examples:
    >>> adjacentElementsProduct([1, 2, 3, 4, 5])
    20
    >>> adjacentElementsProduct([-1, -5, -4, -6, -7])
    42
    >>> adjacentElementsProduct([2, -5, 3])
    -10
    >>> adjacentElementsProduct([2, 4])
    8

    Assumptions:
    - Array of integers
    - 2 <= inputArray.length <= 10
    - -1000 <= inputArray[i] <= 1000

    Arguments:
        inputArray (list): list of integer elements
    Return:
        int: largest product of two adjacent elements
    """

    max_adjacent_product = -math.inf
    for i in range(len(inputArray)-1):
        max_adjacent_product = max(inputArray[i] * inputArray[i+1], max_adjacent_product)

    return max_adjacent_product
