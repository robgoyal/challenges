def matrixElementsSum(matrix):
    """
    Given a rectangular matrix of integers, return the total sum of all
    integers excluding integers that are zero or fall below a zero.
    
    Examples:
    >>> matrixElementsSum([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]])
    9
    
    Assumptions:
    - A value of 0 indicates the room is haunted
    - 1 <= matrix.length <= 5
    - 1 <= matrix[i].length <= 5
    - 0 <= matrix[i][j] <= 10
    
    Arguments:
        matrix (list[list[int]]): 2D rectangular matrix where each element is the cost of the room
    Return:
        int: total cost of available rooms which are not free and are not below the free rooms
    """
    
    haunted_columns = [False] * len(matrix[0])
    
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Add column to haunted
            if matrix[row][col] == 0:
                haunted_columns[col] = True
            # Check if column is not haunted
            elif not haunted_columns[col]:
                total += matrix[row][col]
    
    return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()
