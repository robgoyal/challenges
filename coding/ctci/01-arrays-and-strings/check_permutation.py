def check_permutation(s1, s2):
    """
    Given two strings, write a method to decide if one is
    a permutation of the other.

    A permutation is when two strings have the same characters but
    re-arranged in a different order.

    Assumptions:
    - the character set is ASCII
    - strings can have whitespaces
    - case insensitive permutation matching
    - whitespaces matter
    - case insensitive

    >>> check_permutation("abc", "cba")
    True
    >>> check_permutation("bob", "alice")
    False
    >>> check_permutation("track", "rack")
    False
    >>> check_permutation("", "alice")
    False
    >>> check_permutation("bob", "")
    False
    >>> check_permutation("God", "dog")
    False
    >>> check_permutation("cat ", "act")
    False

    :param s1 (str): string 1
    :param s2 (str): string 2
    :return bool: True or False if s1 and s2 are permutations of each other
    """

    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    for index in range(len(s1)):
        char1 = s1[index]
        char2 = s2[index]

        d1[char1] = d1.get(char1, 0) + 1
        d2[char2] = d2.get(char2, 0) + 1

    return d1 == d2


if __name__ == "__main__":
    import doctest
    doctest.testmod()