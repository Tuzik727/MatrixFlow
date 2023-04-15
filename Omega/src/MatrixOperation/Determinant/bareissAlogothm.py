def determinant_bareiss(matrix):
    """
    Compute the determinant of a matrix using the Bareiss algorithm.

    The Bareiss algorithm is a numerical method for computing the determinant of a matrix
    by performing elementary row operations on the matrix. Unlike the traditional method
    of computing the determinant, which has a time complexity of O(n!), the Bareiss algorithm
    has a time complexity of O(n^3), making it much faster for large matrices.

    Args:
        matrix (list of lists): A square matrix represented as a list of lists, where each
        inner list is a row of the matrix.

    Returns:
        The determinant of the input matrix.

    Raises:
        ValueError: If the input matrix is not square, or if any row has a different number
        of columns than the number of rows.
        ZeroDivisionError: If the algorithm encounters a zero pivot element. This can happen
        if the input matrix is singular.

    Example:
        determinant_bareiss([[1, 2], [3, 4]])  # Returns -2.0
    """
    global det
    n = matrix.rows
    m = matrix.cols

    # Check if matrix is square
    if n != m:
        raise ValueError("Input matrix must be square.")

    # Check if all rows have same length
    for i in range(n):
        if len(matrix[i]) != n:
            raise ValueError("All rows of the input matrix must have the same length.")

    B = [row[:] for row in matrix]

    # Step 1: Compute the determinant of the matrix using the first element in each row
    det = B[0][0]
    for k in range(1, n):
        for i in range(k, n):
            for j in range(k - 1, -1, -1):
                B[i][j] = B[i][j] * B[k - 1][k - 1] - B[k - 1][j] * B[i][k - 1]
            det *= B[k][k]
            B[k][k] = B[k][k] / B[k - 1][k - 1]

            # Step 2: Update the matrix by dividing each element in row k by the pivot element B[k][k]
            for i in range(k + 1, n):
                for j in range(k + 1, n):
                    B[i][j] = (B[k][k] * B[i][j] - B[i][k] * B[k][j]) / B[k][k]

            # Step 3: Check if the pivot element is zero. If it is, the matrix is singular.
            if B[k][k] == 0:
                raise ZeroDivisionError("Zero pivot element encountered. The input matrix may be singular.")

    return det

# Create a copy of the input matrix called B. This is done so that the input matrix is not modified during the
# algorithm. For each row k in the range [0, n-1) (where n is the number of rows in the matrix), perform the
# following steps: For each row i in the range [k+1, n), and for each column j in the range [k+1, n), perform the
# following calculation: Update the element B[i][j] in the B matrix using the following formula: (B[k][k] * B[i][j] -
# B[i][k] * B[k][j]) / B[k][k] This formula is essentially a division-free version of the Gaussian elimination
# algorithm, and is used to eliminate the elements below the diagonal in each column of the matrix. If the element B[
# k][k] is zero, raise a ZeroDivisionError. This is because division by zero is not defined, and the algorithm cannot
# continue. Update the determinant of the matrix by multiplying the current determinant value (B[n-1][n-1]) with the
# previous value of B[k][k]. Store this new value in a variable called det. Swap the values of B[n-1][n-1] and B[k][
# k]. This is done so that the determinant is computed correctly in the next iteration. Return the final determinant
# value stored in det.
