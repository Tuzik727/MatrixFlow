import unittest

from Omega.src.MatrixOperation.Matrix import Matrix
from Omega.src.MatrixOperation.MatrixRank import rank


class RankTestCase(unittest.TestCase):

    def test_rank_of_zero_matrix_is_zero(self):
        # Arrange
        matrix = Matrix(0, 0)

        # Act
        result = rank(matrix)

        # Assert
        self.assertEqual(result, 0)

    def test_rank_of_identity_matrix_is_size(self):
        # Arrange
        matrix = Matrix.identity(3)

        # Act
        result = rank(matrix)

        # Assert
        self.assertEqual(result, 3)

    def test_rank_of_singular_matrix_is_less_than_size(self):
        # Arrange
        matrix = Matrix(3, 3)
        matrix.set_row(0, [1, 2, 3])
        matrix.set_row(1, [4, 5, 6])
        matrix.set_row(2, [7, 8, 9])
        # Act
        result = rank(matrix)

        # Assert
        self.assertEqual(result, 3)

    def test_rank_of_full_rank_matrix_is_size(self):
        # Arrange
        matrix = Matrix(3, 3)
        matrix.set_row(0, [1, 2, 3])
        matrix.set_row(1, [4, 5, 6])
        matrix.set_row(2, [7, 8, 10])

        # Act
        result = rank(matrix)

        # Assert
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
