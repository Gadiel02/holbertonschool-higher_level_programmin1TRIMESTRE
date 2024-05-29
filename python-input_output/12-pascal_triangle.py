def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.
    
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Each element is the sum of the two elements above it
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle
