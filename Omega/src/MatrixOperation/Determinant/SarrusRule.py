def determinant_sarrus(matrix):
    """
    Calculate the determinant of a 3x3 matrix using Sarrus' rule.

    Args:
        matrix (list of lists): A 3x3 matrix represented as a list of lists.

    Returns:
        float: The determinant of the matrix.

    Raises:
        ValueError: If the input matrix is not a 3x3 matrix.
    """

    # Check that the input is a 3x3 matrix
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError('Input must be a 3x3 matrix')

    # Extract the rows of the matrix
    row1, row2, row3 = matrix

    # Apply Sarrus' rule
    term1 = row1[0] * row2[1] * row3[2]
    term2 = row2[0] * row3[1] * row1[2]
    term3 = row3[0] * row1[1] * row2[2]
    term4 = -row1[2] * row2[1] * row3[0]
    term5 = -row2[2] * row3[1] * row1[0]
    term6 = -row3[2] * row1[1] * row2[0]

    return term1 + term2 + term3 + term4 + term5 + term6
