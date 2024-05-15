def square_matrix_simple(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    squared_matrix = [[0] * num_cols for _ in range(num_rows)]
    square = lambda x: x ** 2
    for i in range(num_rows):
        squared_matrix[i] = list(map(square, matrix[i]))
    return squared_matrix
