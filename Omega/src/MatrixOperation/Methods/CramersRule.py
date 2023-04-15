from Omega.src.MatrixOperation.Determinant.bareissAlogothm import determinant_bareiss
from Omega.src.MatrixOperation.Matrix import Matrix
from copy import deepcopy


def cramer_rule(A: Matrix, b: Matrix):
    """
    This method implements Cramer's rule to solve a system of linear equations represented by a matrix A and a vector b.
    Parameters:

    A: Matrix: the coefficient matrix of the system of equations.
    b: Matrix: the vector representing the right-hand side of the system of equations.
    Return:

    If det_A (the determinant of matrix A) is 0, it means that no unique solution exists, so the method returns None.
    Otherwise, it returns a matrix x containing the solution to the system of equations.
    Possible errors and their handling:

    ValueError: This error may be raised if the dimensions of A and b are not compatible. To handle this error,
    you can add a check at the beginning of the method to ensure that the number of rows in A matches the number of
    rows in b. ZeroDivisionError: This error may be raised if det_A is 0. To handle this error, you can return None
    to indicate that no unique solution exists. :param A: :param b: :return:
    """
    n = A.rows
    det_A = determinant_bareiss(A)
    if det_A == 0:
        return None  # No unique solution exists
    x = Matrix(n, n)
    for i in range(n):
        A_i = deepcopy(A)
        A_i[:, i] = b  # replace the i-th column of A with b
        det_A_i = determinant_bareiss(A_i)
        x[i] = det_A_i / det_A
    return x
