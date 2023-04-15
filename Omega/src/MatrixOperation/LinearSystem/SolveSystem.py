import re

from Omega.src.MatrixOperation.Matrix import Matrix
from Omega.src.MatrixOperation.Methods.GJEM import gauss_jordan


def get_equation_coeffs(equation):
    pattern = r'[-+]?\d*\.\d+|[-+]?\d+'  # match any number, including decimals
    constants = []
    try:
        constants = [float(c) for c in re.findall(pattern, equation)]
    except ValueError:
        print("Error: Unable to extract coefficients from equation. Please check the format of the equation and try "
              "again.")
    return constants


def solve_system_2(numbers_list: list, A: Matrix, b: Matrix):
    """
    Solves a system of linear equations using Gauss-Jordan elimination.

    Args:
        numbers_list (List[float]): A list of coefficients and constants in the system of equations.
        A (Matrix): The coefficient matrix of the system of equations.
        b (Matrix): The constant vector of the system of equations.

    Returns:
        A dictionary mapping variable names to their corresponding solutions.

    Raises:
        ValueError: If the number of coefficients and constants in numbers_list is not consistent with the dimensions of A and b.

    """
    n = len(numbers_list)
    rows = A.rows
    # split up equation_list to A and b lists
    A_values = []
    b_values = []
    count = 0
    # if A.rows == 2:
    for i in numbers_list:
        count += 1
        if count == n / 2 or count == n:
            b_values.append(i)
        else:
            A_values.append(i)
    # set the values of matrix A
    for i in range(0, rows):
        if i < rows / 2:
            A.set_row(i, A_values[:n // (rows + 1)])
        else:
            A.set_row(i, A_values[-(n // (rows + 1)):])
    # set the values of vector b
    for i in range(0, rows):
        if i < rows / 2:
            b.set_row(i, b_values[:n // (rows + 2)])
        else:
            b.set_row(i, b_values[-(n // (rows + 2)):])

    # Solve the system of equations using Gauss-Jordan elimination
    try:
        x = gauss_jordan(A, b)
    except:
        raise ValueError("That system doesnt have solution")
    var_names = ['x', 'y', 'z', 'w', 'u', 'v', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't']
    solution = {}
    for i in range(A.cols):
        solution[var_names[i]] = x[i][0]
    return solution


def solve_system_3(numbers_list: list, A: Matrix, b: Matrix):
    """
    Solves a system of linear equations using Gauss-Jordan elimination.

    Args:
        numbers_list (List[float]): A list of coefficients and constants in the system of equations.
        A (Matrix): The coefficient matrix of the system of equations.
        b (Matrix): The constant vector of the system of equations.

    Returns:
        A dictionary mapping variable names to their corresponding solutions.

    Raises:
        ValueError: If the number of coefficients and constants in numbers_list is not consistent with the dimensions of A and b.

    """
    n = len(numbers_list)
    rows = A.rows
    # split up equation_list to A and b lists
    A_values = []
    b_values = []
    count = 0
    # adding values to A and b matrix's
    for i in numbers_list:
        count += 1
        if count == 4:
            b_values.append(i)
            count = 0
        else:
            A_values.append(i)

    # set the values of matrix A for 3 rows
    for i in range(rows):
        if i == 0:
            A.set_row(0, A_values[:3])
        elif i == 1:
            A.set_row(1, A_values[3:6])
        elif i == 2:
            A.set_row(2, A_values[6:])

    # set the values of vector b
    b.set_row(0, b_values[:1])
    b.set_row(1, b_values[1:2])
    b.set_row(2, b_values[2:3])

    # Solve the system of equations using Gauss-Jordan elimination
    x = gauss_jordan(A, b)

    var_names = ['x', 'y', 'z', 'w', 'u', 'v', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't']
    solution = {}
    for i in range(A.cols):
        solution[var_names[i]] = x[i][0]
    return solution


def solve_system_4(numbers_list: list, A: Matrix, b: Matrix):
    """
    Solves a system of linear equations using Gauss-Jordan elimination.

    Args:
        numbers_list (List[float]): A list of coefficients and constants in the system of equations.
        A (Matrix): The coefficient matrix of the system of equations.
        b (Matrix): The constant vector of the system of equations.

    Returns:
        A dictionary mapping variable names to their corresponding solutions.

    Raises:
        ValueError: If the number of coefficients and constants in numbers_list is not consistent with the dimensions of A and b.

    """
    n = len(numbers_list)
    rows = A.rows
    # split up equation_list to A and b lists
    A_values = []
    b_values = []
    count = 0
    # adding values to A and b matrix's
    for i in numbers_list:
        count += 1
        if count == 5:
            b_values.append(i)
            count = 0
        else:
            A_values.append(i)

    # set the values of matrix A for 3 rows
    for i in range(rows):
        if i == 0:
            A.set_row(0, A_values[:4])
        elif i == 1:
            A.set_row(1, A_values[4:8])
        elif i == 2:
            A.set_row(2, A_values[8:12])
        elif i == 3:
            A.set_row(3, A_values[12:16])

    # set the values of vector b
    b.set_row(0, b_values[:1])
    b.set_row(1, b_values[1:2])
    b.set_row(2, b_values[2:3])
    b.set_row(3, b_values[3:4])

    print("A:", A)
    print("b:", b)

    # Solve the system of equations using Gauss-Jordan elimination
    x = gauss_jordan(A, b)

    var_names = ['x', 'y', 'z', 'w', 'u', 'v', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't']
    solution = {}
    for i in range(A.cols):
        solution[var_names[i]] = x[i][0]
    return solution
