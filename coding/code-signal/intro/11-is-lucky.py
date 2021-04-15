def isLucky(n):
    """
    Given a ticket number n, determine if its lucky or not. 
    
    A ticket number is lucky if the sum of the first half of the digits
    is equal to the sum of the second half.
    
    Assumptions:
    - n is a positive integer with an even number of digits
    - 10 <= n <= 10^6
    
    Arguments:
        n (int): ticket number
    Return:
        bool: True if n is lucky, False otherwise
        
    Examples:
    >>> isLucky(10)
    False
    >>> isLucky(1230)
    True
    """
    
    strn = str(n) 
    midpoint = len(strn) // 2
 
    first_half = strn[:midpoint]
    second_half = strn[midpoint:]

    return sum(int(c) for c in first_half) == sum(int(c) for c in second_half)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

