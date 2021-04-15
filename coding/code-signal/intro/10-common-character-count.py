def commonCharacterCount(s1, s2):
    """
    Given two strings, find the number of common characters between them.
    
    Arguments:
        s1 (str): string 1
        s2 (str): string 2
    Return:
        int: number of common characters
        
    Assumptions:
    - strings consist of lowercase english letters
    - 1 <= s1.length <= 15
    - 1 <= s2.length <= 15
    
    Examples:
    >>> commonCharacterCount("aabcc", "adcaa")
    3
    >>> commonCharacterCount("abc", "cba")
    3
    >>> commonCharacterCount("aaabcc", "aadddc")
    3
    """
    
    common = dict.fromkeys(string.ascii_lowercase, [0, 0])

    for char in s1:
        common[char][0] += 1
    for char in s2:
        common[char][1] += 1
    
    return sum(min(counts) for counts in common.values())


if __name__ == "__main__":
    import doctest
    doctest.testmod()

