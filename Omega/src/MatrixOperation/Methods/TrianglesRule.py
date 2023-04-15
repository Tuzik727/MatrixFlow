class TriangularMatrix:
    """
    The TriangularMatrix class represents a square triangular matrix. The class constructor takes two parameters:

    n: an integer representing the size of the matrix (number of rows/columns). triangular_type: a string representing
    the type of triangular matrix to create. It can be either 'upper' for an upper triangular matrix or 'lower' for a
    lower triangular matrix.


    __getitem__(self, index): allows indexing into the matrix using the square bracket notation. It returns the row at the specified index.
    __setitem__(self, index, value): allows updating values in the matrix using the square bracket notation. It sets the value at the specified index to the given value.
    __str__(self): returns a string representation of the matrix. It prints each row on a separate line, with the elements in the row separated by spaces.
    __repr__(self): returns a string representation of the matrix, which is the same as __str__(self).
    __len__(self): returns the size of the matrix (number of rows/columns).
    """
    def __init__(self, n, triangular_type='upper'):
        self.n = n
        self.triangular_type = triangular_type
        self.matrix = [[0] * n for _ in range(n)]
        if self.triangular_type == 'upper':
            for i in range(n):
                for j in range(i, n):
                    self.matrix[i][j] = 0
        elif self.triangular_type == 'lower':
            for i in range(n):
                for j in range(0, i + 1):
                    self.matrix[i][j] = 0
        else:
            raise ValueError("Invalid triangular matrix type. Must be 'upper' or 'lower'.")

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.matrix])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.n
