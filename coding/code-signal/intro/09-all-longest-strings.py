def allLongestStrings(inputArray):
    """
    Given an array of strings, return another array containing all of its longest strings.
    
    Assumptions:
    - inputArray is non-empty
    - the return of the strings should be in the same order
    
    Examples:
    >>> allLongestStrings(["aba", "aa", "ad", "vcd", "aba"])
    ["aba", "vcd", "aba"]
    
    Arguments:
        inputArray (list[str]): list of strings
    Return:
        list[str]: longest list of strings in inputArray
    """
    
    # List of strings related to size
    buckets = {}
    
    for s in inputArray:
        slen = len(s)
        if slen in buckets:
            buckets[slen].append(s)
        else:
            buckets[slen] = [s]
    
    return buckets[max(buckets)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
