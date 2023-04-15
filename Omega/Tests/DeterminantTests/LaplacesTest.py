import unittest

from Omega.src.MatrixOperation.Determinant.Determinant import determinant
from Omega.src.MatrixOperation.Matrix import Matrix


class TestDeterminant(unittest.TestCase):

    def test_determinant_2x2(self):
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        self.assertEqual(determinant(matrix), -2)

    def test_determinant_3x3(self):
        matrix = Matrix(3, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3
        matrix[1, 0] = 4
        matrix[1, 1] = 5
        matrix[1, 2] = 6
        matrix[2, 0] = 7
        matrix[2, 1] = 8
        matrix[2, 2] = 9
        self.assertEqual(determinant(matrix), 0)

    def test_determinant_non_square_matrix(self):
        matrix = Matrix(2, 3)
        with self.assertRaises(ValueError):
            determinant(matrix)


if __name__ == '__main__':
    unittest.main()