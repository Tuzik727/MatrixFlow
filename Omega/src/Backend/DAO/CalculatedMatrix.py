import pyodbc

from Omega.src.Backend.MatrixDB import MatrixDB
from Omega.src.MatrixOperation.Matrix import Matrix
from datetime import datetime


class CalculatedMatrixDAO:
    def __init__(self, matrix: Matrix, operation, matrixID):
        values = ' '.join([str(cell) for row in matrix for cell in row])
        self.Rows = matrix.rows
        self.Cols = matrix.cols
        self.Value = values
        self.mOperation = operation
        self.matrixID = matrixID
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor

    def insert_calculated_matrix(self):
        """
        Inserts a new calculated matrix into the database.

        Raises:
            sqlite3.Error: If there is an error executing the query.
        """
        try:
            self.matrixDB.execute_query(
                "INSERT INTO CalculatedMatrix(_Rows, _Column, _Value, MatrixOperation, matrixID, DateCreated) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (self.Rows, self.Cols, self.Value, self.mOperation, self.matrixID,
                 datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

            print("Matrix inserted successfully. Calculated Matrix ID: ")
        except pyodbc.Error as e:
            self.matrixDB.conn.rollback()
            print("Error inserting matrix:", e)
        finally:
            print("Rows inserted: ", self.matrixDB.cursor.rowcount)

    def delete_calculated_matrix(self, matrix_id):
        """
        Deletes a calculated matrix from the database.

        Args:
            matrix_id (int): The ID of the matrix to delete.

        Raises:
            sqlite3.Error: If there is an error executing the query.
        """
        try:
            self.matrixDB.execute_query(
                "DELETE FROM CalculatedMatrix WHERE CalculatedMatrixID = ?", (matrix_id,))
            print("Calculated Matrix deleted successfully")
        except pyodbc.Error as e:
            self.matrixDB.conn.rollback()
            print("Error deleting matrix:", e)
        finally:
            print("Rows deleted: ", self.matrixDB.cursor.rowcount)

    def update_calculated_matrix(self, new_matrix: Matrix, new_operation):
        """
        Update an existing calculated matrix with a new matrix and a new operation.

        Args:
            new_matrix (Matrix): The new matrix to be stored in the database.
            new_operation (str): The new operation to be associated with the matrix.

        Returns:
            None

        Raises:
            Exception: If an error occurs while updating the calculated matrix.
        """
        try:
            # Flatten the new matrix and join its values into a string.
            new_values = ' '.join([str(cell) for row in new_matrix for cell in row])

            # Update the existing calculated matrix in the database.
            self.matrixDB.execute_query(
                "UPDATE CalculatedMatrix SET _Rows = ?, _Column = ?, _Value = ?, MatrixOperation = ? "
                "WHERE CalculatedMatrixID = ?",
                (new_matrix.rows, new_matrix.cols, new_values, new_operation, self.matrixID))

            print("Calculated Matrix updated successfully")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating matrix:", e)
            raise
        finally:
            print("Rows updated: ", self.matrixDB.cursor.rowcount)

