from src.MatrixOperation.Matrix import Matrix
from src.MatrixOperation.MatrixRank import rank
from src.MatrixOperation.Determinant.bareissAlogothm import determinant_bareiss
import json


# from flask import request


class MatrixUI:
    def __init__(self):
        self.matrix = None
        self.equations = []  # Define the equations attribute

    def create_matrix(self, rows, cols, matrix_data):
        matrix = Matrix(rows, cols)
        if isinstance(matrix_data, list):
            for i in range(rows):
                row_values = matrix_data[i]
                if len(row_values) != cols:
                    raise ValueError("Invalid number of elements in row.")
                matrix.set_row(i, row_values)
        elif isinstance(matrix_data, dict):
            for i in range(rows):
                row_values = matrix_data.get(f"row{i}", "").split()
                if len(row_values) != cols:
                    raise ValueError("Invalid number of elements in row.")
                matrix.set_row(i, [int(val) for val in row_values])
        else:
            raise ValueError("Invalid matrix data type.")
        return matrix

    def deserialize_matrix(self, json_str):
        json_dict = json.loads(json_str)
        print(json_dict)
        matrix_data = json_dict.get('matrix', [])
        print(matrix_data)
        rows = json_dict.get('rows')
        cols = json_dict.get('cols')
        matrix = Matrix(rows, cols)
        if isinstance(matrix_data, list):
            for i in range(rows):
                row_values = matrix_data[i]
                if len(row_values) != cols:
                    raise ValueError("Invalid number of elements in row.")
                matrix.set_row(i, row_values)
        else:
            raise ValueError("Invalid matrix data type in JSON dict.")

        self.matrix = matrix
        print(self.matrix)
        return matrix  # added return statement

    def display_matrix(self):
        if self.matrix is None:
            print("Matrix not created yet.")
        else:
            print("Matrix:\n" + str(self.matrix))

    def display_shape(self):
        return

    def display_rank(self):
        return rank(self.matrix)

    def display_inverse(self):
        if self.matrix is None:
            print("Matrix not created yet.")
        else:
            inverse_matrix = self.matrix.inverse()
            if inverse_matrix is None:
                print("This matrix is not invertible.")
            else:
                print("Inverse matrix:\n" + str(inverse_matrix))

    def display_transpose(self):
        if self.matrix is None:
            print("Matrix not created yet.")
        else:
            transpose_matrix = self.matrix.transpose()
            if transpose_matrix is None:
                print("This matrix is not invertible.")
            else:
                print("Transpose matrix:\n" + str(transpose_matrix))

    def add_matrices(self):
        other_matrix = self.create_other_matrix()
        if self.matrix is None:
            print("Matrix not created yet.")
        elif self.matrix.shape() != other_matrix.shape():
            print("Matrices must have the same shape.")
        else:
            result_matrix = self.matrix + other_matrix
            print("Result:\n" + str(result_matrix))

    def subtract_matrices(self):
        other_matrix = self.create_other_matrix()
        if self.matrix is None:
            print("Matrix not created yet.")
        elif self.matrix.shape() != other_matrix.shape():
            print("Matrices must have the same shape.")
        else:
            result_matrix = self.matrix - other_matrix
            print("Result:\n" + str(result_matrix))

    def multiply_matrices(self):
        other_matrix = self.create_other_matrix()
        if self.matrix is None:
            print("Matrix not created yet.")
        elif self.matrix.shape()[1] != other_matrix.shape()[0]:
            print("The number of columns in the first matrix must equal the number of rows in the second matrix.")
        else:
            result_matrix = self.matrix @ other_matrix
            print("Result:\n" + str(result_matrix))

    def divide_matrix(self):
        if self.matrix is None:
            print("Matrix not created yet.")
        else:
            while True:
                try:
                    scalar = int(input("Enter a scalar value to divide the matrix by: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            result_matrix = self.matrix / scalar
            print("Result:\n" + str(result_matrix))

    def pow(self):
        while True:
            try:
                power = int(input("Enter a power value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        result_matrix = self.matrix.pow(power)
        print("Result:\n" + str(result_matrix))

    def matrix_rank(self, matrix: Matrix):
        return rank(matrix)

    def matrix_determinant(self, matrix: Matrix):
        return determinant_bareiss(matrix)

    def create_other_matrix(self):
        while True:
            try:
                rows = int(input("Enter the number of rows for the other matrix: "))
                cols = int(input("Enter the number of columns for the other matrix: "))
                if rows <= 0 or cols <= 0:
                    print("Invalid input. Please enter values greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter integers.")

        other_matrix = Matrix(rows, cols)

        for i in range(rows):
            while True:
                try:
                    row_values = input(f"Enter values for row {i + 1}, separated by spaces: ")
                    row_values = [int(value) for value in row_values.split()]
                    if len(row_values) != cols:
                        print(f"Invalid input. Please enter {cols} values.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter integers.")

            other_matrix.set_row(i, row_values)

        return other_matrix

    def display_determinant(self):
        print(determinant_bareiss(self.matrix))

    def run(self):
        while True:
            print("\nSelect an option:")
            print("1. Create a matrix")
            print("2. Matrix operations")
            print("3. Solve a system of linear equations")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_matrix()
            elif choice == 2:
                self.matrix_operations()
            elif choice == 3:
                self.display_linear_system()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

    def matrix_operations(self):
        while True:
            print("\nSelect an operation:")
            print("1. Display the matrix")
            print("2. Display the shape of the matrix")
            print("3. Display the rank of the matrix")
            print("4. Display the inverse of the matrix")
            print("5. Display the transpose of the matrix")
            print("6. Add matrices")
            print("7. Subtract matrices")
            print("8. Multiply matrices")
            print("9. Divide matrix by scalar")
            print("10. Power")
            print("11. Calculate determinant of the matrix")
            print("12. Return to main menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.display_matrix()
            elif choice == 2:
                self.display_shape()
            elif choice == 3:
                self.display_rank()
            elif choice == 4:
                self.display_inverse()
            elif choice == 5:
                self.display_transpose()
            elif choice == 6:
                self.add_matrices()
            elif choice == 7:
                self.subtract_matrices()
            elif choice == 8:
                self.multiply_matrices()
            elif choice == 9:
                self.divide_matrix()
            elif choice == 10:
                self.pow()
            elif choice == 11:
                self.display_determinant()
            elif choice == 12:
                break
            else:
                print("Invalid choice. Please try again.")
