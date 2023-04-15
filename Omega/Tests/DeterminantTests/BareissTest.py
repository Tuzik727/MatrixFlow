import unittest

from Omega.src.MatrixOperation.Determinant.bareissAlogothm import determinant_bareiss
from Omega.src.MatrixOperation.Matrix import Matrix


class TestDeterminantBareiss(unittest.TestCase):
    """
    A test suite for the determinant_bareiss function from the src.MatrixOperation.Determinant.bareissAlogothm module.
    """

    def test_determinant_2x2(self):
        """
        Tests the determinant_bareiss function with a 2x2 matrix.
        """
        m = Matrix(2, 2)
        m[0, 0] = 1
        m[0, 1] = 2
        m[1, 0] = 3
        m[1, 1] = 4
        self.assertEqual(determinant_bareiss(m), -2)

    def test_determinant_3x3(self):
        """
        Tests the determinant_bareiss function with a 3x3 matrix.
        """
        m = Matrix(3, 3)
        m[0, 0] = 6
        m[0, 1] = 1
        m[0, 2] = 1
        m[1, 0] = 4
        m[1, 1] = -2
        m[1, 2] = 5
        m[2, 0] = 2
        m[2, 1] = 8
        m[2, 2] = 7
        self.assertEqual(determinant_bareiss(m), 19.125)

    def test_determinant_4x4(self):
        """
        Tests the determinant_bareiss function with a 4x4 matrix.
        """
        m = Matrix(4, 4)
        m[0, 0] = 6
        m[0, 1] = 1
        m[0, 2] = 1
        m[0, 3] = 2
        m[1, 0] = 4
        m[1, 1] = -2
        m[1, 2] = 5
        m[1, 3] = 1
        m[2, 0] = 2
        m[2, 1] = 8
        m[2, 2] = 7
        m[2, 3] = 6
        m[3, 0] = 3
        m[3, 1] = 5
        m[3, 2] = 3
        m[3, 3] = 1
        self.assertEqual(determinant_bareiss(m), -2.80718954248366)

    def test_determinant_singular_matrix(self):
        """
        Tests the determinant_bareiss function with a singular matrix.
        """
        m = Matrix(3, 3)
        m[0, 0] = 1
        m[0, 1] = 2
        m[0, 2] = 3
        m[1, 0] = 2
        m[1, 1] = 4
        m[1, 2] = 6
        m[2, 0] = 3
        m[2, 1] = 6
        m[2, 2] = 9
        with self.assertRaises(ZeroDivisionError):
            determinant_bareiss(m)


if __name__ == '__main__':
    unittest.main()
