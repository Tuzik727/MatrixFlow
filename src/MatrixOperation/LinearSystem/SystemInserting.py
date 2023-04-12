from src.Backend.DAO.Equations import EquationDAO
from src.Backend.DAO.Solutions import SolutionDAO
from src.Backend.DAO.Systems import SystemsDAO
from src.MatrixOperation.LinearSystem.SolveSystem import solve_system_2, solve_system_3, get_equation_coeffs, \
    solve_system_4
from src.MatrixOperation.Matrix import Matrix


def insertLinearSystem(equations_str: str, userID: int):
    """
    Inserts a linear system into the database and calculates the solution.

    Args:
    - equations_str: a string representing the system of linear equations, where each equation is separated by a newline character.
    - userID: an integer representing the ID of the user who created the system.

    Returns:
    - None

    Raises:
    - ValueError: if the number of equations in the system is not between 2 and 4, inclusive.
    - TypeError: if the equations_str or userID is not of the expected type.
    - Exception: if there is an error inserting the system into the database or calculating the solution.

    """
    global solution
    try:
        equations_list = equations_str.split('\n')
        num_rows = len(equations_list)

        # Initialize matrices A and b
        A = Matrix(num_rows, num_rows)
        b = Matrix(num_rows, 1)

        if num_rows == 2:
            # Insert system into the database
            System_2 = SystemsDAO("equation of two variables", userID)
            System_2.insert_system()
            systemID = System_2.getLastSystemID()

            # Solve the system and insert equations and solutions into the database
            solution = solve_system_2(get_equation_coeffs(equations_str), A, b)
            Equations = EquationDAO(equations_str, systemID)
            Solutions = SolutionDAO(systemID, str(f"{solution.get('x')} {solution.get('y')}"))
            Equations.insert_equation()
            Solutions.insert_solution()

        elif num_rows == 3:
            # Insert system into the database
            System_3 = SystemsDAO("equation of three variables", userID)
            System_3.insert_system()
            systemID = System_3.getLastSystemID()

            # Solve the system and insert equations and solutions into the database
            solution = solve_system_3(get_equation_coeffs(equations_str), A, b)
            Equations = EquationDAO(equations_str, systemID)
            Solutions = SolutionDAO(systemID, str(f"{solution.get('x')} {solution.get('y')} {solution.get('z')}"))
            Equations.insert_equation()
            Solutions.insert_solution()

        elif num_rows == 4:
            # Insert system into the database
            System_4 = SystemsDAO("equation of four variables", userID)
            System_4.insert_system()
            systemID = System_4.getLastSystemID()

            # Solve the system and insert equations and solutions into the database
            solution = solve_system_4(get_equation_coeffs(equations_str), A, b)
            Equations = EquationDAO(equations_str, systemID)
            Solutions = SolutionDAO(systemID,
                                    str(f"{solution.get('x')} {solution.get('y')} {solution.get('z')} {solution.get('w')}"))
            Equations.insert_equation()
            Solutions.insert_solution()

        else:
            raise ValueError("The number of equations in the system must be between 2 and 4, inclusive.")

        return solution

    except ValueError as ve:
        # Catch ValueError and re-raise with appropriate message
        raise ve

    except TypeError as te:
        # Catch TypeError and re
        raise te


