from Omega.src.MatrixOperation.Matrix import Matrix


def determinant(matrix: Matrix) -> float:
    """
    Calculate the determinant of a square matrix using the Laplace expansion method.

    Args:
        matrix (Matrix): The square matrix to calculate the determinant of.

    Returns:
        float: The determinant of the matrix.

    Raises:
        ValueError: If the matrix is not square.
    """

    if not matrix.is_square():
        raise ValueError('Matrix must be square')

    if matrix.rows == 1:
        return matrix[0, 0]

    if matrix.rows == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    # Laplace's expansion along the first row
    det = 0
    for j in range(matrix.cols):
        sign = (-1) ** j
        minor = Matrix(matrix.rows - 1, matrix.cols - 1)
        for i in range(1, matrix.rows):
            row = matrix[i, :]
            minor_row = row[:j] + row[j + 1:]
            minor.set_row(i - 1, minor_row)
        det += sign * matrix[0, j] * determinant(minor)

    return det
