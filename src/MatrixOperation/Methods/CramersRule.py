from src.MatrixOperation.Determinant.bareissAlogothm import determinant_bareiss
from src.MatrixOperation.Matrix import Matrix
from copy import deepcopy


def cramer_rule(A: Matrix, b: Matrix):
    n = A.rows
    det_A = determinant_bareiss(A)
    if det_A == 0:
        return None  # No unique solution exists
    x = Matrix(n)
    for i in range(n):
        A_i = deepcopy(A)
        A_i[:, i] = b  # replace the i-th column of A with b
        det_A_i = determinant_bareiss(A_i)
        x[i] = det_A_i / det_A
    return x
