from src.MatrixOperation.Matrix import Matrix


def inverse(self):
    # Check if the matrix is square
    if self.rows != self.cols:
        raise ValueError("Matrix is not square and doesn't have an inverse.")

    # Create an augmented matrix with an identity matrix appended to the right
    aug_matrix = [[0 for j in range(self.cols * 2)] for i in range(self.rows)]
    for i in range(self.rows):
        for j in range(self.cols):
            aug_matrix[i][j] = self.matrix[i][j]
        aug_matrix[i][self.cols + i] = 1

    # Use Gauss-Jordan elimination to transform the left half of the augmented matrix to the identity matrix
    for i in range(self.rows):
        # Find pivot row
        pivot_row = i
        for j in range(i, self.rows):
            if abs(aug_matrix[j][i]) > abs(aug_matrix[pivot_row][i]):
                pivot_row = j

        # Check if pivot element is zero
        pivot = aug_matrix[pivot_row][i]
        if pivot == 0:
            raise ValueError("Matrix is not invertible.")

        # Swap pivot row with current row (if needed)
        if pivot_row != i:
            aug_matrix[i], aug_matrix[pivot_row] = aug_matrix[pivot_row], aug_matrix[i]

        # Reduce pivot row
        for j in range(self.cols * 2):
            aug_matrix[i][j] /= pivot

        # Reduce other rows
        for j in range(self.rows):
            if j != i:
                factor = aug_matrix[j][i]
                for k in range(self.cols * 2):
                    aug_matrix[j][k] -= factor * aug_matrix[i][k]

    # Extract the inverse matrix from the right half of the augmented matrix
    inverse_matrix = [[0 for j in range(self.cols)] for i in range(self.rows)]
    for i in range(self.rows):
        for j in range(self.cols):
            inverse_matrix[i][j] = aug_matrix[i][j + self.cols]

    return Matrix(self.rows, self.cols, inverse_matrix)