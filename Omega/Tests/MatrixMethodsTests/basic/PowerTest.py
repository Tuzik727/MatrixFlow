import unittest

from Omega.src.MatrixOperation.Matrix import Matrix


class TestPow(unittest.TestCase):
    def test_pow_with_zero_power(self):
        # Test raising matrix to the power of 0
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4

        expected = Matrix.identity(2)
        result = matrix.pow(0)

        self.assertEqual(result, expected)

    def test_pow_with_identity_matrix(self):
        # Test raising identity matrix to the power of any number
        matrix = Matrix.identity(3)

        expected = Matrix.identity(3)
        result = matrix.pow(5)

        self.assertEqual(result, expected)

    def test_pow_with_odd_power(self):
        # Test raising matrix to an odd power
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4

        expected = Matrix(2, 2)
        expected[0, 0] = 37
        expected[0, 1] = 54
        expected[1, 0] = 81
        expected[1, 1] = 118

        result = matrix.pow(3)

        self.assertEqual(result, expected)

    def test_pow_with_even_power(self):
        # Test raising matrix to an even power
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4

        expected = Matrix(2, 2)
        expected[0, 0] = 199
        expected[0, 1] = 290
        expected[1, 0] = 435
        expected[1, 1] = 634

        result = matrix.pow(4)

        self.assertEqual(result, expected)

    def test_pow_with_non_square_matrix(self):
        # Test raising non-square matrix to a power
        matrix = Matrix(2, 3)
        matrix.set_row(0, [1, 2, 3])
        matrix.set_row(1, [4, 5, 6])

        with self.assertRaises(ValueError):
            result = matrix.pow(2)


if __name__ == '__main__':
    unittest.main()
