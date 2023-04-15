from Omega.src.MatrixOperation.Matrix import Matrix
from copy import deepcopy


# Finding inverse matrix using montante
def montante(matrix):
    """
     Compute the inverse of a square matrix using Montante's method.
     Args:
         matrix: A square matrix of size n x n.
     Returns:
         The inverse of the input matrix.
     Raises:
         ValueError: If the input matrix is not square.
     """
    if not matrix.is_square():
        raise ValueError("Matrix must be square to find its inverse using Montante's method")

    # Make a copy of the input matrix to avoid modifying it
    n = matrix.rows
    A = deepcopy(matrix)
    B = Matrix.identity(n)

    # Apply Montante's method to the augmented matrix [A|I]
    for i in range(n):
        # Set A[i,i] to 1 by dividing the ith row by A[i,i]
        A[i, i] = 1

        for j in range(i + 1, n):
            # If A[j,i] is 0, skip this row
            if A[j, i] == 0:
                continue

            # Compute the factor to eliminate A[j,i] using the ith row
            c = A[j, i] / A[i, i]

            # Update the jth row of A and B
            for k in range(i, n):
                A[j, k] = A[j, k] - c * A[i, k]
            for k in range(n):
                B[j, k] = B[j, k] - c * B[i, k]

    # Back-substitute to eliminate the entries above the main diagonal
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            # If A[j,i] is 0, skip this row
            if A[j, i] == 0:
                continue

            # Compute the factor to eliminate A[j,i] using the ith row
            c = A[j, i] / A[i, i]

            # Update the jth row of A and B
            for k in range(i, n):
                A[j, k] = A[j, k] - c * A[i, k]
            for k in range(n):
                B[j, k] = B[j, k] - c * B[i, k]

    # Normalize the rows of B by the diagonal entries of A
    for i in range(n):
        d = A[i, i]
        for j in range(n):
            B[i, j] = B[i, j] / d

    return B

# This function takes a single argument matrix, which is a square matrix of size n x n. It first creates a copy of
# the input matrix using the deepcopy method from the copy module. It then creates a new matrix B that is the
# identity matrix of the same size as the input matrix. The function then performs the forward phase of Montante's
# method, which involves subtracting multiples of one row from another row to create zeros in the lower-left part of
# the matrix. This is done using nested loops, with the outer loop iterating over the rows of the matrix and the
# inner loops iterating over the columns. The function checks for zeros in the pivot positions to avoid division by
# zero errors. After the forward phase is complete, the function performs the backward phase, which involves
# subtracting multiples of one row from another row to create zeros in the upper-right part of the matrix. This is
# done using similar nested loops. Finally, the function divides each row of the matrix B by the diagonal element of
# the corresponding row of the matrix A to obtain the inverse matrix. If the input matrix is not square, the function
# raises a ValueError with an appropriate error message. The function returns the inverse of the input matrix as a
# new matrix.
