import json


class Matrix:
    """
    A class representing a matrix of numbers with rows and columns.

    Attributes:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        matrix (list): The 2D list of numbers representing the matrix.

    Methods:
        __getitem__(self, index): Get an element or a slice of the matrix.
        __setitem__(self, index, value): Set an element or a slice of the matrix.
        __str__(self): Convert the matrix to a string.
        shape(self): Get the shape of the matrix as a tuple of (rows, columns).
        set_submatrix(self, start_row, start_col, matrix): Set a submatrix of the matrix.
        set_column(self, index, column_values): Set a column of the matrix.
        is_square(self): Check if the matrix is square.
        rank(self): Get the rank of the matrix using Gauss-Jordan elimination.
        inverse(self): Get the inverse of the matrix using Gauss-Jordan elimination.
    """

    def __init__(self, rows, cols):
        """
        Initialize a matrix with the given number of rows and columns.

        Args:
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.

        Raises: ValueError: If either `rows` or `cols` is not a positive integer.
        """
        if not isinstance(rows, int) or not isinstance(cols, int) or rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive integers")

        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        """ getitem(self, index): Retrieve the value(s) at the given index or indices from the matrix.
        Args:
            index: An int or tuple of ints representing the index or indices to retrieve. If an int is provided, the corresponding row of the matrix will be returned as a list. If a tuple is provided, the corresponding element in the matrix will be returned.

        Returns:
            The value(s) at the specified index or indices.

        Raises:
            TypeError: If the index is not an int or tuple of ints.
            IndexError: If the index is out of range for the matrix.
        """
        if isinstance(index, int):
            return self.matrix[index]
        else:
            row, col = index
            try:
                return self.matrix[row][col]
            except IndexError:
                # If the index is out of range, raise an IndexError
                raise IndexError("Index out of range for matrix")

    def __setitem__(self, index, value):
        """
        Set an element or a slice of the matrix.

        Args:
            index (int or tuple): The index or slice to set.
            value (int or list): The value or slice to set.

        Returns:
            None
        """
        if isinstance(index, int):
            try:
                self.matrix[index] = value
            except IndexError:
                raise IndexError("Index out of range for matrix")
        elif isinstance(index, tuple) and len(index) == 2:
            row, col = index
            try:
                if isinstance(value, int):
                    self.matrix[row][col] = value
                elif isinstance(value, list) and len(value) == self.cols:
                    self.matrix[row] = value
                else:
                    raise TypeError("Value must be an int or a list of ints with length equal to number of columns")
            except IndexError:
                raise IndexError("Index out of range for matrix")
        else:
            raise TypeError("Index must be an int or a tuple of two ints")

    def __str__(self):
        """
        Convert the matrix to a string.

        Returns:
            A string representation of the matrix.

        Raises:
            TypeError: If the matrix contains non-numeric elements.
        """
        rows = []
        for row in self.matrix:
            row_str = " ".join(str(elem) for elem in row)
            rows.append(row_str)
        return "\n".join(rows)

    def __add__(self, other):
        """
        Add another matrix or scalar to this matrix.

        Args:
            other (Matrix or int or float): The matrix or scalar to add.

        Returns:
            A new matrix representing the sum.

        Raises:
            TypeError: If `other` is not a Matrix or a numeric scalar.
            ValueError: If the shape of the matrix to be added is not the same as this matrix.
        """
        if isinstance(other, Matrix):
            if self.shape() != other.shape():
                raise ValueError("Matrix dimensions do not match for addition")
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other[i, j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other
            return result
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Matrix' and '{}'".format(type(other)))

    def __sub__(self, other):
        """
        Subtract another matrix or scalar from this matrix.

        Args:
            other (Matrix or int or float): The matrix or scalar to subtract.

        Returns:
            A new matrix representing the difference.

        Raises:
            TypeError: If `other` is not a Matrix or a numeric scalar.
            ValueError: If the shape of the matrix to be subtracted is not the same as this matrix.
        """
        if isinstance(other, Matrix):
            if self.shape() != other.shape():
                raise ValueError("Matrix dimensions do not match for subtraction")
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other[i, j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other
            return result
        else:
            raise TypeError("Unsupported operand type for -: %s" % type(other).__name__)

    def __eq__(self, other):
        """
        Check if two matrices are equal.

        Args:
            other (Matrix): The matrix to compare to.

        Returns:
            bool: True if the two matrices are equal, False otherwise.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type for ==: %s" % type(other).__name__)

        if self.shape() != other.shape():
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self[i, j] != other[i, j]:
                    return False

        return True

    def __truediv__(self, scalar):
        """
        Divide all elements of the matrix by a scalar.

        Args:
            scalar (int or float): The scalar value to divide by.

        Returns:
            Matrix: A new matrix with the elements divided by the scalar.

        Raises:
            ZeroDivisionError: If the scalar value is zero.

        """
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix[i][j] = self[i][j] / scalar
        return result_matrix

    def __rmul__(self, other):
        """
        Define the right multiplication operation, for when a scalar is on the left.

        Args:
            other (float/int): The scalar to multiply with.

        Returns:
            Matrix: A new matrix with the scalar multiplied to each element.

        Raises:
            TypeError: If the scalar is not a float or integer.
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Unsupported operand type for *: '{}' and 'Matrix'".format(type(other).__name__))

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] * other
        return result

    def __mul__(self, other):
        """
        Define the matrix multiplication operation with another matrix or a scalar.

        Args:
            other (Matrix or float/int): The other matrix or scalar to multiply with.

        Returns:
            Matrix: A new matrix resulting from the multiplication.

        Raises:
            TypeError: If other is not a Matrix or scalar.
            ValueError: If the matrices' dimensions do not match for multiplication.
        """
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix dimensions do not match for multiplication")

            result = Matrix(self.rows, other.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    for k in range(self.cols):
                        result[i, j] += self[i, k] * other[k, j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] * other
            return result
        else:
            raise TypeError("Unsupported operand type for *: 'Matrix' and '{}'".format(type(other).__name__))

    def __matmul__(self, other):
        """
        Define the matrix multiplication operation, for when the @ operator is used between two matrices.

        Args:
            other (Matrix): The matrix to multiply with.

        Returns:
            Matrix: A new matrix resulting from the matrix multiplication.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type(s) for @: 'Matrix' and '{}'".format(type(other).__name__))

        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                for k in range(self.cols):
                    result[i, j] += self[i, k] * other[k, j]
        return result

    def __repr__(self):
        return repr(self.matrix)

    def serialize_matrix(self):
        """
        Serialize the matrix object to a JSON string.

        Returns:
            str: A JSON string representing the matrix object.
        """
        try:
            return json.dumps({
                "matrix": self.matrix,
                "rows": self.rows,
                "cols": self.cols
            })
        except Exception as e:
            raise ValueError("Unable to serialize matrix: {}".format(str(e)))

    # json_dict = {'matrix_data': [[1, 2], [3, 4]], 'rows': 2, 'cols': 2, 'equations': []}

    def argmax(self):
        """
        Find the index of the maximum element in the matrix.

        Returns:
            tuple: The index of the maximum element in the matrix.
        """
        rows = self.rows
        cols = self.cols
        if not self.matrix:
            raise ValueError("Matrix is empty")
        max_val = self.matrix[0][0]
        max_idx = (0, 0)
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] > max_val:
                    max_val = self.matrix[i][j]
                    max_idx = (i, j)
        return max_idx

    def abs(self):
        new_data = [[abs(element) for element in row] for row in self.data]
        return Matrix(new_data)

    def zeros(self):
        """
        Creates a new matrix of the same dimensions as the current matrix,
        filled with zeros.

        Returns:
            Matrix: A new matrix with the same dimensions as the current matrix,
            but filled with zeros instead.
        """
        return Matrix(self.rows, self.cols)

    def reshape(self, rows, cols):
        """
        Reshape the matrix into a new shape.

        Args:
            rows (int): The number of rows for the new shape.
            cols (int): The number of columns for the new shape.

        Raises:
            ValueError: If the new shape has more elements than the original shape.
            ValueError: If the new shape has fewer elements than the original shape.

        Returns:
            None.
        """
        num_elements = rows * cols
        if num_elements != self.rows * self.cols:
            raise ValueError("Total number of elements must remain constant during reshaping.")

        flattened = [elem for row in self.matrix for elem in row]
        new_matrix = []
        for i in range(rows):
            row = flattened[i * cols: (i + 1) * cols]
            new_matrix.append(row)
        self.matrix = new_matrix

    def hstack(self, other):
        """
        Stack two matrices horizontally (i.e., column-wise).

        Args:
            other (Matrix): The matrix to stack.

        Returns:
            Matrix: The stacked matrix.

        Raises:
            ValueError: If matrices have different number of rows.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type for hstack(): %s" % type(other).__name__)

        if self.rows != other.rows:
            raise ValueError("Matrices have different number of rows.")

        new_matrix = Matrix(self.rows, self.cols + other.cols)
        for i in range(self.rows):
            new_matrix.set_row(i, self.matrix[i] + other.matrix[i])

        return new_matrix

    def shape(self):
        """
        Return the shape of the matrix as a tuple of (rows, columns).

        Returns:
            Tuple[int, int]: The shape of the matrix.

        Raises:
            ValueError: If the matrix is empty.
        """
        if self.rows == 0 or self.cols == 0:
            raise ValueError("Matrix is empty.")

        return self.rows, self.cols

    def set_submatrix(self, start_row, start_col, matrix):
        """
        Set a submatrix of the matrix.

        Args:
            start_row (int): The starting row index of the submatrix.
            start_col (int): The starting column index of the submatrix.
            matrix (Matrix): The matrix to set as a submatrix.

        Returns:
            None

        Raises:
            ValueError: If the submatrix is out of bounds.
            TypeError: If the input matrix is not a Matrix object.
        """
        if not isinstance(matrix, Matrix):
            raise TypeError("Unsupported operand type for set_submatrix(): %s" % type(matrix).__name__)

        end_row = start_row + matrix.rows
        end_col = start_col + matrix.cols
        if end_row > self.rows or end_col > self.cols or start_row < 0 or start_col < 0:
            raise ValueError("Submatrix is out of bounds.")

        for i in range(matrix.rows):
            for j in range(matrix.cols):
                self[start_row + i, start_col + j] = matrix[i, j]

    def set_column(self, index, column_values):
        """
        Set the values of a column in the matrix.

        Args:
            index (int): The index of the column to set.
            column_values (list): The list of values to set the column to.

        Returns:
            None

        Raises:
            ValueError: If the length of column_values is not equal to the number of rows in the matrix.
        """
        if len(column_values) != self.rows:
            raise ValueError("Length of column_values does not match number of rows in matrix.")

        for i in range(self.rows):
            self.matrix[i][index] = column_values[i]

    def is_square(self):
        """
        Check if the matrix is square (i.e., has the same number of rows and columns).

        Returns:
            bool: True if the matrix is square, False otherwise.
        """
        return self.rows == self.cols

    def set_element(self, row, col, value):
        """
        Set a single element of the matrix.

        Args:
            row (int): The row index of the element.
            col (int): The column index of the element.
            value (int): The value to set the element to.

        Returns:
            None
        """
        self.matrix[row][col] = value

    def set_row(self, index, row_values):
        """
        Set a row of the matrix.

        Args:
            index (int): The index of the row to set.
            row_values (list): The list of values to set in the row.

        Returns:
            None
        """
        self.matrix[index] = row_values

    def pow(self, power):
        """
        Raise the matrix to the given power.

        Args:
            power (int): The power to raise the matrix to.

        Returns:
            Matrix: The result of raising the matrix to the given power.
        """
        if not self.is_square():
            raise ValueError("Matrix must be square to raise to a power")

        if power == 0:
            return Matrix.identity(self.rows)
        elif power == 1:
            return self
        else:
            square = self @ self
            if power % 2 == 0:
                return square.pow(power // 2)
            else:
                return self @ square.pow((power - 1) // 2)

    def transpose(self):
        """
        Return the transpose of the matrix.

        Returns:
            Matrix: The transpose of the matrix.
        """
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result[j, i] = self[i, j]
        return result

    def inverse(self):
        """
        Computes the inverse of the matrix using Gauss-Jordan elimination.

        Returns:
            Matrix: The inverse of the matrix.

        Raises:
            ValueError: If the matrix is not square or is singular (i.e., has no inverse).
        """
        # Check if the matrix is square
        if self.rows != self.cols:
            raise ValueError("Matrix is not square and doesn't have an inverse.")

        # Create an augmented matrix with an identity matrix appended to the right
        aug_matrix = [[0 for _ in range(self.cols * 2)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                aug_matrix[i][j] = self.matrix[i][j]
            aug_matrix[i][self.cols + i] = 1

        # Use Gauss-Jordan elimination to transform the left half of the augmented matrix to the identity matrix
        for i in range(self.rows):
            # Find pivot row
            pivot_row = i
            for j in range(i, self.rows):
                if abs(aug_matrix[j][i]) > abs(aug_matrix[pivot_row][i]):
                    pivot_row = j

            # Check if pivot element is zero
            pivot = aug_matrix[pivot_row][i]
            if pivot == 0:
                raise ValueError("Matrix is not invertible.")

            # Swap pivot row with current row (if needed)
            if pivot_row != i:
                aug_matrix[i], aug_matrix[pivot_row] = aug_matrix[pivot_row], aug_matrix[i]

            # Reduce pivot row
            for j in range(self.cols * 2):
                aug_matrix[i][j] /= pivot

            # Reduce other rows
            for j in range(self.rows):
                if j != i:
                    factor = aug_matrix[j][i]
                    for k in range(self.cols * 2):
                        aug_matrix[j][k] -= factor * aug_matrix[i][k]

        # Extract the inverse matrix from the right half of the augmented matrix
        inverse_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                inverse_matrix[i][j] = aug_matrix[i][j + self.cols]

        return inverse_matrix

    def identity(self, n):
        """
        Returns an n x n identity matrix.

        Args:
            n (int): The size of the identity matrix.

        Returns:
            Matrix: An n x n identity matrix.
        """
        identity_matrix = Matrix(n, n)
        for i in range(n):
            identity_matrix[i, i] = 1
        return identity_matrix

    def multiply_by_scalar(self, scalar):
        """
        Multiply the matrix by a scalar value.

        Args:
            scalar (int or float): The scalar value to multiply the matrix by.

        Returns:
            None
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        for i in range(self.rows):
            for j in range(self.cols):
                self[i, j] *= scalar

    def set_element(self, i, j, value):
        """
        Set a single element of the matrix.

        Args:
            i (int): The row index of the element.
            j (int): The column index of the element.
            value (int): The value to set the element to.

        Returns:
            None
        """
        self.matrix[i][j] = value
