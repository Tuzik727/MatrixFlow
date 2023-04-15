import unittest

from Omega.src.MatrixOperation.Matrix import Matrix


class TestInverse(unittest.TestCase):
    def test_inverse_of_2x2_matrix(self):
        # Test inverse of a 2x2 matrix
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        expected = [[-2.0, 1.0], [1.5, -0.5]]
        result = matrix.inverse()
        rounded_result = [[round(val, 2) for val in row] for row in result]
        self.assertEqual(rounded_result, expected)

    def test_inverse_of_3x3_matrix(self):
        # Test inverse of a 3x3 matrix
        matrix = Matrix(3, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3
        matrix[1, 0] = 0
        matrix[1, 1] = 1
        matrix[1, 2] = 4
        matrix[2, 0] = 5
        matrix[2, 1] = 6
        matrix[2, 2] = 0
        expected = [[-24.0, 18.0, 5.0], [20.0, -15.0, -4.0], [-5.0, 4.0, 1.0]]
        result = matrix.inverse()
        rounded_result = [[round(val, 2) for val in row] for row in result]
        self.assertEqual(rounded_result, expected)

    def test_inverse_of_singular_matrix(self):
        # Test inverse of a singular matrix (non-invertible)
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 2
        matrix[1, 1] = 4
        with self.assertRaises(ValueError):
            result = matrix.inverse()

    def test_inverse_of_non_square_matrix(self):
        # Test inverse of a non-square matrix
        matrix = Matrix(2, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3
        matrix[1, 0] = 4
        matrix[1, 1] = 5
        matrix[1, 2] = 6
        with self.assertRaises(ValueError):
            result = matrix.inverse()


if __name__ == '__main__':
    unittest.main()
