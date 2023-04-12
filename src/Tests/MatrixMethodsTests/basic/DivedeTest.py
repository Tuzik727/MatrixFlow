import unittest

from src.MatrixOperation.Matrix import Matrix


class TestMatrixDivide(unittest.TestCase):

    def test_divide_scalar(self):
        m = Matrix(2, 2)
        m[0, 0] = 2
        m[0, 1] = 4
        m[1, 0] = 6
        m[1, 1] = 8

        result = m / 2

        expected = Matrix(2, 2)
        expected[0, 0] = 1
        expected[0, 1] = 2
        expected[1, 0] = 3
        expected[1, 1] = 4

        self.assertEqual(result, expected)

    def test_divide_scalar_zero(self):
        m = Matrix(2, 2)
        m[0, 0] = 2
        m[0, 1] = 4
        m[1, 0] = 6
        m[1, 1] = 8

        with self.assertRaises(ZeroDivisionError):
            m / 0

    def test_divide_scalar_negative(self):
        m = Matrix(2, 2)
        m[0, 0] = 2
        m[0, 1] = 4
        m[1, 0] = 6
        m[1, 1] = 8

        result = m / -2

        expected = Matrix(2, 2)
        expected[0, 0] = -1
        expected[0, 1] = -2
        expected[1, 0] = -3
        expected[1, 1] = -4

        self.assertEqual(result, expected)

    def test_divide_scalar_fraction(self):
        m = Matrix(2, 2)
        m[0, 0] = 2
        m[0, 1] = 4
        m[1, 0] = 6
        m[1, 1] = 8

        result = m / 0.5

        expected = Matrix(2, 2)
        expected[0, 0] = 4
        expected[0, 1] = 8
        expected[1, 0] = 12
        expected[1, 1] = 16

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
