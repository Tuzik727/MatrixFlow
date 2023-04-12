from src.MatrixOperation.Matrix import Matrix
from copy import deepcopy


# Finding inverse matrix using montante
def montante(matrix):
    if not matrix.is_square():
        raise ValueError("Matrix must be square to find its inverse using Montante's method")
    n = matrix.rows
    A = deepcopy(matrix)
    B = Matrix.identity(n)
    for i in range(n):
        A[i, i] = 1
        for j in range(i + 1, n):
            if A[j, i] == 0:
                continue
            c = A[j, i] / A[i, i]
            for k in range(i, n):
                A[j, k] = A[j, k] - c * A[i, k]
            for k in range(n):
                B[j, k] = B[j, k] - c * B[i, k]
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if A[j, i] == 0:
                continue
            c = A[j, i] / A[i, i]
            for k in range(i, n):
                A[j, k] = A[j, k] - c * A[i, k]
            for k in range(n):
                B[j, k] = B[j, k] - c * B[i, k]
    for i in range(n):
        d = A[i, i]
        for j in range(n):
            B[i, j] = B[i, j] / d
    return B
