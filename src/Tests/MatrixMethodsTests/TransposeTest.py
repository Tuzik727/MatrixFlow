import unittest

from src.MatrixOperation.Matrix import Matrix


class TestMatrixTranspose(unittest.TestCase):

    def test_transpose_square_matrix(self):
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

        expected_result = Matrix(3, 3)
        expected_result[0, 0] = 1
        expected_result[0, 1] = 4
        expected_result[0, 2] = 7
        expected_result[1, 0] = 2
        expected_result[1, 1] = 5
        expected_result[1, 2] = 8
        expected_result[2, 0] = 3
        expected_result[2, 1] = 6
        expected_result[2, 2] = 9

        self.assertEqual(matrix.transpose(), expected_result)

    def test_transpose_rectangular_matrix(self):
        matrix = Matrix(2, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3
        matrix[1, 0] = 4
        matrix[1, 1] = 5
        matrix[1, 2] = 6

        expected_result = Matrix(3, 2)
        expected_result[0, 0] = 1
        expected_result[0, 1] = 4
        expected_result[1, 0] = 2
        expected_result[1, 1] = 5
        expected_result[2, 0] = 3
        expected_result[2, 1] = 6

        self.assertEqual(matrix.transpose(), expected_result)

    def test_transpose_single_row_matrix(self):
        matrix = Matrix(1, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3

        expected_result = Matrix(3, 1)
        expected_result[0, 0] = 1
        expected_result[1, 0] = 2
        expected_result[2, 0] = 3

        self.assertEqual(matrix.transpose(), expected_result)

    def test_transpose_single_col_matrix(self):
        matrix = Matrix(3, 1)
        matrix[0, 0] = 1
        matrix[1, 0] = 2
        matrix[2, 0] = 3

        expected_result = Matrix(1, 3)
        expected_result[0, 0] = 1
        expected_result[0, 1] = 2
        expected_result[0, 2] = 3

        self.assertEqual(matrix.transpose(), expected_result)

    def test_transpose_empty_matrix(self):
        matrix = Matrix(0, 0)

        expected_result = Matrix(0, 0)

        self.assertEqual(matrix.transpose(), expected_result)


if __name__ == '__main__':
    unittest.main()
