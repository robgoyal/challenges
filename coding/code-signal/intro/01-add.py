def add(param1, param2):
    """
    Return the sum of two values
    
    Examples:
    >>> add(1, 2)
    3
    
    Arguments:
        param1 (int): integer
        param2 (int): integer
    Return:
        int: sum of param1 and param2
    """
    
    return param1 + param2


if __name__ == "__main__":
    import doctest; doctest.testmod()
