class TriangularMatrix:
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
