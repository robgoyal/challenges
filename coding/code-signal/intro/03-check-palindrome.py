def checkPalindrome(inputString):
    """
    Return True if the inputString is a palindrome, False otherwise.
    
    Examples:
    >>> checkPalindrome("racecar")
    True
    >>> checkPalindrome("abac")
    False
    >>> checkPalindrom("a")
    True
    
    Assumptions:
    - inputString is non-empty
    - inputString consists of lowercase characters
    - 1 <= inputString.length <= 10^5
    
    Arguments:
        inputString (str): string to check if palindrome
    Return:
        bool: boolean if inputString is palindrome
    """
    
    fptr = 0
    bptr = len(inputString) - 1
    
    while (fptr < bptr):
        if inputString[fptr] != inputString[bptr]:
            return False
        fptr += 1
        bptr -= 1
    
    return True


if __name__ == "__main__":
    import doctest; doctest.testmod()

