from src.MatrixOperation.Matrix import Matrix
from src.MatrixOperation.DiagonalMatrix import diagonal_matrix


def lu_decomposition(matrix: Matrix):
    """
    Perform LU decomposition of a given matrix using Gaussian elimination.
    Args:
        matrix: A square matrix of size n x n.
    Returns:
        A tuple of matrices (L, U) such that A = L*U.
    """
    n = matrix.rows
    L = diagonal_matrix(n)
    U = matrix

    for i in range(n - 1):
        for j in range(i + 1, n):
            if U[j, i] != 0:
                ratio = U[i, i] / U[j, i]
                L[j, i] = ratio
                U[j] = U[j] * ratio - U[i]

    return L, U
