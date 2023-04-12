import unittest

from src.MatrixOperation.Matrix import Matrix


class TestMatrixMultiplication(unittest.TestCase):
    def test_scalar_multiplication(self):
        # [1, 2], [3, 4]]
        # Test scalar multiplication on a matrix
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4

        result = matrix * 2
        # [[2, 4], [6, 8]]
        expected = Matrix(2, 2)
        expected[0, 0] = 2
        expected[0, 1] = 4
        expected[1, 0] = 6
        expected[1, 1] = 8

        self.assertEqual(result, expected)

    def test_matrix_multiplication(self):
        # Test matrix multiplication between two matrices
        matrix1 = Matrix(2, 2)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[1, 0] = 3
        matrix1[1, 1] = 4

        matrix2 = Matrix(2, 2)
        matrix2[0, 0] = 5
        matrix2[0, 1] = 6
        matrix2[1, 0] = 7
        matrix2[1, 1] = 8

        result = matrix1 * matrix2
        expected = Matrix(2, 2)
        expected[0, 0] = 19
        expected[0, 1] = 22
        expected[1, 0] = 43
        expected[1, 1] = 50

        self.assertEqual(result, expected)

    def test_scalar_right_multiplication(self):
        # Test scalar multiplication on a matrix using right multiplication
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        result = 2 * matrix

        expected = Matrix(2, 2)

        expected[0, 0] = 2
        expected[0, 1] = 4
        expected[1, 0] = 6
        expected[1, 1] = 8
        self.assertEqual(result, expected)

    def test_scalar_right_multiplication_with_non_scalar(self):
        # Test scalar right multiplication with a non-scalar
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        with self.assertRaises(TypeError):
            result = matrix.__rmul__(matrix)

    def test_matrix_multiplication_with_wrong_dimensions(self):
        # Test matrix multiplication with incompatible dimensions
        matrix1 = Matrix(2, 2)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[1, 0] = 3
        matrix1[1, 1] = 4

        matrix2 = Matrix(2, 3)
        matrix2.set_row(0, [1, 2, 3])
        matrix2.set_row(1, [4, 5, 6])

        with self.assertRaises(ValueError):
            matrix1.__mul__(matrix2)


if __name__ == '__main__':
    unittest.main()
