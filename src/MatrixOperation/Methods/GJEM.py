from src.MatrixOperation.Matrix import Matrix
from fraction import Fraction

def gauss_jordan(A: Matrix, b: Matrix):
    n = A.rows
    Ab = [[float(A[i][j]) for j in range(n)] + [float(b[i][0])] for i in range(n)]
    for i in range(n):
        max_row = i
        max_val = Ab[i][i]
        for j in range(i + 1, n):
            if Ab[j][i] > max_val:
                max_row = j
                max_val = Ab[j][i]
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]
        for j in range(i + 1, n):
            c = Ab[j][i] / Ab[i][i]
            for k in range(i + 1, n + 1):
                Ab[j][k] -= c * Ab[i][k]
    for i in range(n - 1, -1, -1):
        for j in range(i):
            c = Ab[j][i] / Ab[i][i]
            for k in range(n, i - 1, -1):
                Ab[j][k] -= c * Ab[i][k]
        Ab[i][n] /= Ab[i][i]
        Ab[i][i] = 1
    return [[Ab[i][n]] for i in range(n)]
