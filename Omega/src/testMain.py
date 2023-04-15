from Omega.src.MatrixOperation.Matrix import Matrix

A = Matrix(3, 3)
A.set_row(0, [1, 2, 3])
A.set_row(1, [4, 5, 6])
A.set_row(2, [7, 8, 9])

B = Matrix(3, 3)
A.set_row(0, [1, 2, 3])
A.set_row(1, [4, 5, 6])
A.set_row(2, [7, 8, 9])

print(A.identity(3))
