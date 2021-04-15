def is_sequential(sequence):
    """
    Return True is a sequence is sequential, False otherwise.
    
    Arguments:
        sequence (list): sequence
    Return:
        bool: True if sequential, False othewise
    """
    
    for i in range(len(sequence) - 1):
        if sequence[i + 1] <= sequence[i]:
            return False
    return True

def almostIncreasingSequence(sequence):
    """
    Return True or False if an array can be sequential by
    removing no more than one element from the array.
    
    Examples:
    >>> almostIncreasingSequence([1, 3, 2, 1])
    False
    >>> almostIncreasingSequence([1, 3, 2])
    True
    >>> almostIncreasingSequence([1, 2, 1, 2])
    False
    >>> almostIncreasingSequence([2, 1])
    True

    Assumptions:
    - 2 <= sequence.length <= 10^5
    - -10^5 <= sequence[i] <= 10^5
    
    Arguments:
        sequence (list): list of integers
    Return:
        bool: True or False if the array be sequential by a single removal
    """
    
    for i in range(len(sequence) - 1):
        if sequence[i + 1] <= sequence[i]:
            # Test removing current
            remove_curr_seq = is_sequential(sequence[:i] + sequence[i+1:]) 
            
            remove_next_seq = True
            if i != (len(sequence) - 2):
                remove_next_seq = is_sequential(sequence[:i+1] + sequence[i+2:])
            
            if not remove_curr_seq and not remove_next_seq:
                return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
