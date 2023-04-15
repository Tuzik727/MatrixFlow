from Omega.src.MatrixOperation.Matrix import Matrix


def diagonal_matrix(n):
    """
    Create a diagonal matrix from a list of values.
    Args:
        values: A 1D array of values to be placed on the diagonal.
    Returns:
        A square diagonal matrix of size n x n, where n is the length of values.
        param n: DF
    """
    matrix = Matrix(n, n)
    values = []
    for j in range(n):
        values.append(1)

    for i in range(n):
        matrix[i, i] = values[i]
    return matrix

