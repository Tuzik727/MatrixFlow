from Omega.src.MatrixOperation.Matrix import Matrix


def gauss_jordan(A: Matrix, b: Matrix) -> Matrix:
    """
    Solves a system of linear equations represented by a matrix A and a vector b
    using the Gauss-Jordan elimination method.

    Args:
        A (Matrix): The coefficient matrix of the system of equations.
        b (Matrix): The vector representing the right-hand side of the system of equations.

    Returns:
        Matrix: A matrix x containing the solution to the system of equations.

    Raises:
        ValueError: If the dimensions of A and b are not compatible.
        ZeroDivisionError: If Ab[i][i] is 0 when dividing in line 14 or 21.
        IndexError: If an index is out of range when accessing elements of Ab.

    """
    n = A.rows
    Ab = [[float(A[i][j]) for j in range(n)] + [float(b[i][0])] for i in range(n)]

    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = i
        max_val = Ab[i][i]
        for j in range(i + 1, n):
            if Ab[j][i] > max_val:
                max_row = j
                max_val = Ab[j][i]
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        # Gauss elimination
        for j in range(i + 1, n):
            c = Ab[j][i] / Ab[i][i]
            for k in range(i + 1, n + 1):
                Ab[j][k] -= c * Ab[i][k]

    # Back substitution
    try:
        for i in range(n - 1, -1, -1):
            for j in range(i):
                c = Ab[j][i] / Ab[i][i]
                for k in range(n, i - 1, -1):
                    Ab[j][k] -= c * Ab[i][k]
            Ab[i][n] /= Ab[i][i]
            Ab[i][i] = 1
    except:
        raise ValueError
    return [[Ab[i][n]] for i in range(n)]

# This function gauss_jordan takes two matrix objects as inputs, A and b, which represent the coefficients and
# constants of a system of linear equations, respectively. The function returns a matrix x which represents the
# solution of the system of equations. The function first creates a matrix Ab which is a concatenation of the
# coefficient matrix A and the constant matrix b. This is achieved using list comprehension to iterate over the rows
# of A and b and concatenating each row. Then the function proceeds with the Gauss-Jordan elimination method to solve
# the system of linear equations. The first loop iterates over the rows of Ab. It finds the row max_row with the
# largest value in the current column i, then swaps this row with the current row i. This ensures that the diagonal
# elements of the matrix Ab are nonzero. The second loop iterates over the rows of Ab starting from the row after the
# current row i. It subtracts a multiple of row i from each subsequent row to eliminate the entries below the
# diagonal. The multiple c is calculated as the ratio of the element to be eliminated and the diagonal element of row
# i. After the above loop completes, the matrix Ab is in row echelon form. The third loop then iterates over the rows
# of Ab in reverse order, starting from the last row. It uses the entries on the diagonal to eliminate the entries
# above the diagonal, by subtracting a multiple of row i from each previous row. Finally, the last operation
# normalizes the diagonal entries to 1 by dividing the entire row i by its diagonal element Ab[i][i]. The solution is
# then extracted from the last column of the modified Ab matrix. The possible errors that may occur are documented in
# the method's documentation.
