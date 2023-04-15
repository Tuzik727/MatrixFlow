import unittest

from Omega.src.MatrixOperation.Determinant.SarrusRule import determinant_sarrus
from Omega.src.MatrixOperation.Matrix import Matrix


class TestDeterminantSarrus(unittest.TestCase):

    def test_determinant_3x3(self):
        m = Matrix(3, 3)
        m[0, 0] = 1
        m[0, 1] = 2
        m[0, 2] = 3
        m[1, 0] = 4
        m[1, 1] = 5
        m[1, 2] = 6
        m[2, 0] = 7
        m[2, 1] = 8
        m[2, 2] = 9
        self.assertEqual(determinant_sarrus(m), 0)

    def test_determinant_3x3_negative(self):
        m = Matrix(3, 3)
        m[0, 0] = -1
        m[0, 1] = -2
        m[0, 2] = -3
        m[1, 0] = -4
        m[1, 1] = -5
        m[1, 2] = -6
        m[2, 0] = -7
        m[2, 1] = -8
        m[2, 2] = -9
        self.assertEqual(determinant_sarrus(m), 0)

    def test_determinant_3x3_zero(self):
        m = Matrix(3, 3)
        m[0, 0] = 0
        m[0, 1] = 0
        m[0, 2] = 0
        m[1, 0] = 0
        m[1, 1] = 0
        m[1, 2] = 0
        m[2, 0] = 0
        m[2, 1] = 0
        m[2, 2] = 0
        self.assertEqual(determinant_sarrus(m), 0)

    def test_determinant_3x3_positive(self):
        m = Matrix(3, 3)
        m[0, 0] = 1
        m[0, 1] = 2
        m[0, 2] = 3
        m[1, 0] = 2
        m[1, 1] = 3
        m[1, 2] = 4
        m[2, 0] = 5
        m[2, 1] = 6
        m[2, 2] = 7
        self.assertEqual(determinant_sarrus(m), 0)


if __name__ == '__main__':
    unittest.main()
