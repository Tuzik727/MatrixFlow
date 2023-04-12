from copy import deepcopy


def rank(matrix):
    """
    Calculate the rank of a matrix using the Gauss-Jordan elimination method.

    Parameters:
        matrix (Matrix): A matrix to calculate the rank of

    Returns:
        The rank of the input matrix
    """
    # Check input matrix is not empty
    if not matrix:
        raise ValueError("Input matrix is empty.")

    # Make a copy of the input matrix
    rref = deepcopy(matrix)

    # Iterate over rows
    for i in range(matrix.rows):
        # Find pivot row
        pivot_row = i
        for j in range(i, matrix.rows):
            if abs(rref[j][i]) > abs(rref[pivot_row][i]):
                pivot_row = j

        # Check if pivot element is zero
        pivot = rref[pivot_row][i]
        if pivot == 0:
            break

        # Swap pivot row with current row (if needed)
        if pivot_row != i:
            rref[i], rref[pivot_row] = rref[pivot_row], rref[i]

        # Reduce pivot row
        for j in range(matrix.cols):
            rref[i][j] /= pivot

        # Reduce other rows
        for j in range(matrix.rows):
            if j != i:
                factor = rref[j][i]
                for k in range(matrix.cols):
                    rref[j][k] -= factor * rref[i][k]

    # Count the number of non-zero rows
    rank = sum([any(rref[i][j] != 0 for j in range(matrix.cols)) for i in range(matrix.rows)])

    return rank
