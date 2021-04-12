def centuryFromYear(year):
    """
    Return the century given a year. 
    
    Examples:
    >>> centuryFromYear(1)
    1
    >>> centuryFromYear(800)
    8
    >>> centuryFromYear(799)
    8
    
    Assumptions:
        - 1 <= year <= 2005
    
    Args:
        year (int): year
    Returns:
        int: century
    """
    
    return year // 100 + (0 if year % 100 == 0 else 1)


if __name__ == "__main__":
    import doctest; doctest.testmod()
