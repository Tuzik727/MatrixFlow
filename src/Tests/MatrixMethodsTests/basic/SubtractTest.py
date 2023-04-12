import unittest

from src.MatrixOperation.Matrix import Matrix


class TestMatrixSub(unittest.TestCase):
    def test_subtract_matrix(self):
        matrix1 = Matrix(2, 3)
        matrix1[0, 0] = 1
        matrix1[0, 1] = 2
        matrix1[0, 2] = 3
        matrix1[1, 0] = 4
        matrix1[1, 1] = 5
        matrix1[1, 2] = 6

        matrix2 = Matrix(2, 3)
        matrix2[0, 0] = 7
        matrix2[0, 1] = 8
        matrix2[0, 2] = 9
        matrix2[1, 0] = 10
        matrix2[1, 1] = 11
        matrix2[1, 2] = 12

        expected_result = Matrix(2, 3)
        expected_result[0, 0] = -6
        expected_result[0, 1] = -6
        expected_result[0, 2] = -6
        expected_result[1, 0] = -6
        expected_result[1, 1] = -6
        expected_result[1, 2] = -6

        result = matrix1 - matrix2

        for i in range(result.rows):
            for j in range(result.cols):
                self.assertEqual(result[i, j], expected_result[i, j])

    def test_subtract_scalar(self):
        matrix = Matrix(2, 3)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[0, 2] = 3
        matrix[1, 0] = 4
        matrix[1, 1] = 5
        matrix[1, 2] = 6

        expected_result = Matrix(2, 3)
        expected_result[0, 0] = 0
        expected_result[0, 1] = 1
        expected_result[0, 2] = 2
        expected_result[1, 0] = 3
        expected_result[1, 1] = 4
        expected_result[1, 2] = 5

        self.assertEqual(matrix - 1, expected_result)

    def test_subtract_mismatched_shapes(self):
        matrix1 = Matrix(2, 3)
        matrix2 = Matrix(3, 2)

        with self.assertRaises(ValueError):
            matrix1 - matrix2

    def test_subtract_unsupported_type(self):
        matrix = Matrix(2, 3)

        with self.assertRaises(TypeError):
            matrix - "string"
