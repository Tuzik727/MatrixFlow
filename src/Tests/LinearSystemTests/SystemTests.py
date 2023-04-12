import unittest

from src.MatrixOperation.LinearSystem.SolveSystem import solve_system_2, get_equation_coeffs, solve_system_3, \
    solve_system_4
from src.MatrixOperation.Matrix import Matrix


class TestSolveSystem2(unittest.TestCase):

    def test_solve_system_2(self):
        A = Matrix(2, 2)
        b = Matrix(2, 1)

        numbers_list = [2, 3, 4, 5, 6, 7]
        expected_solution = {'x': -1.0, 'y': 2.0}
        solution = solve_system_2(numbers_list, A, b)
        self.assertEqual(round(solution.get("x")), expected_solution.get("x"))
        self.assertEqual(round(solution.get("y")), expected_solution.get("y"))

    def test_solve_system_3(self):
        A = Matrix(3, 3)
        b = Matrix(3, 1)

        numbers_list = [1, -2, 3, 7, 2, 1, 1, 4, -3, 2, -2, -10]
        expected_solution = {'x': 2.0, 'y': -1.0, 'z': 1.0}
        solution = solve_system_3(numbers_list, A, b)
        self.assertAlmostEqual(round(solution.get("x")), expected_solution.get("x"), places=7)
        self.assertAlmostEqual(round(solution.get("y")), expected_solution.get("y"), places=7)
        self.assertAlmostEqual(round(solution.get("z")), expected_solution.get("z"), places=7)
        self.assertEqual(len(solution), len(expected_solution), "Number of solutions should match")

    def test_solve_system_4(self):
        A = Matrix(4, 4)
        b = Matrix(4, 1)

        numbers_list = [1, 2, 1, -1, 5, 3/2, 1, 2, 2, 8, 4, 4, 3, 4, 22, 2/5, 0, 1/5, 1, 3]
        expected_solution = {'x': 16, 'y': -6, 'z': -2, 'w': -3}
        solution = solve_system_4(numbers_list, A, b)
        self.assertAlmostEqual(round(solution.get("x")), expected_solution.get("x"), places=7)
        self.assertAlmostEqual(round(solution.get("y")), expected_solution.get("y"), places=7)
        self.assertAlmostEqual(round(solution.get("z")), expected_solution.get("z"), places=7)
        self.assertAlmostEqual(round(solution.get("w")), expected_solution.get("w"), places=7)
        self.assertEqual(len(solution), len(expected_solution), "Number of solutions should match")

    def test_get_equation_coeffs(self):
        equation = '2x + 3y = 6'
        expected_coeffs = [2.0, 3.0, 6.0]
        self.assertEqual(get_equation_coeffs(equation), expected_coeffs)


if __name__ == '__main__':
    unittest.main()
