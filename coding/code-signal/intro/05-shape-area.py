def shapeArea(n):
    """
    Return the area of an n-interesting polygon.

    Examples:
    >>> shapeArea(1)
    1
    >>> shapeArea(2)
    5
    >>> shapeArea(3)
    13
    >>> shapeArea(4)
    25

    Assumptions:
    - 1 <= n <= 10^4

    Arguments:
        n (int): integer
    Return:
        int: area of the n-interesting polygon
    """

    total = 1
    for i in range(1, n):
        total += (4 * i)
    return total
 