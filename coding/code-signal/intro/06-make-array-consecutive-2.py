def makeArrayConsecutive2(statues):
    """
    Determine the number of statues required to make the array consecutive.
    
    Examples:
    >>> makeArrayConsecutive2([6, 2, 3, 8])
    3
    >>> makeArrayConsecutive2([1, 5, 9, 15])
    11
    
    
    Assumptions:
    - each element in statues in distinct
    - each element is a non-negative integer
    - 1 <= statues.length <= 10
    - 0 <= statues[i] <= 20
    
    Arguments:
        statues (list): array of non-negative integers
    Return:
        int: minimal number of statues needed
    """
    
    return max(statues) - min(statues) - (len(statues) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

