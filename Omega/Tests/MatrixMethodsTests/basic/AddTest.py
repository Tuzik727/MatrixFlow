import unittest

from Omega.src.MatrixOperation.Matrix import Matrix


class TestMatrixAdd(unittest.TestCase):
    def test_add(self):
        # Test adding two matrices with the same dimensions
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

        result = matrix1 + matrix2

        self.assertEqual(result[0, 0], 6)
        self.assertEqual(result[0, 1], 8)
        self.assertEqual(result[1, 0], 10)
        self.assertEqual(result[1, 1], 12)

    def test_add_different_dimensions(self):
        # Test adding two matrices with different dimensions
        matrix1 = Matrix(2, 2)
        matrix2 = Matrix(3, 3)

        with self.assertRaises(ValueError):
            matrix1 + matrix2

    def test_add_scalar(self):
        # Test adding a scalar to a matrix
        matrix1 = Matrix(2, 2)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[1, 0] = 3
        matrix1[1, 1] = 4

        scalar = 5

        result = matrix1 + scalar

        self.assertEqual(result[0, 0], 6)
        self.assertEqual(result[0, 1], 7)
        self.assertEqual(result[1, 0], 8)
        self.assertEqual(result[1, 1], 9)

    def test_add_zero(self):
        # Test adding a zero matrix to another matrix
        matrix1 = Matrix(2, 2)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[1, 0] = 3
        matrix1[1, 1] = 4

        matrix2 = Matrix(2, 2)

        result = matrix1 + matrix2

        self.assertEqual(result[0, 0], 1)
        self.assertEqual(result[0, 1], 2)
        self.assertEqual(result[1, 0], 3)
        self.assertEqual(result[1, 1], 4)

    def test_add_identity(self):
        # Test adding an identity matrix to another matrix
        matrix1 = Matrix(2, 2)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[1, 0] = 3
        matrix1[1, 1] = 4

        matrix2 = Matrix.identity(2)

        result = matrix1 + matrix2

        self.assertEqual(result[0, 0], 2)
        self.assertEqual(result[0, 1], 2)
        self.assertEqual(result[1, 0], 3)
        self.assertEqual(result[1, 1], 5)


if __name__ == '__main__':
    unittest.main()
