from Omega.src.MatrixOperation.Matrix import Matrix
from Omega.src.Backend.MatrixDB import MatrixDB
from datetime import datetime


class MatrixDAO:
    """
    Data access object for Matrix table in the database
    """
    def __init__(self, matrix: Matrix, UserID):
        """
        Initializes the MatrixDAO object

        Args:
            matrix (Matrix): The matrix object to be inserted/updated in the database
            UserID (int): The user ID associated with the matrix
        """
        values = ' '.join([str(cell) for row in matrix for cell in row])
        self.Rows = matrix.rows
        self.Cols = matrix.cols
        self.Values = values
        self.UserID = UserID
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor
        self.matrixID = None

    def insert_matrix(self):
        """
        Inserts the matrix object into the database
        """
        try:
            self.matrixDB.execute_query("INSERT INTO Matrix(_Rows, _Column, _Value, UserID, DateCreated) values (?, "
                                        "?, ?, ?, ?)",
                                        (self.Rows, self.Cols, self.Values, self.UserID, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            # Retrieve the last inserted matrix ID
            matrix_id = self.matrixDB.execute_query("SELECT TOP 1 MatrixID FROM Matrix ORDER BY MatrixID DESC")
            self.matrixID = matrix_id
            print("Matrix inserted successfully. Matrix ID: ", matrix_id)

        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error inserting matrix:", e)
        finally:
            print("Rows inserted: ", self.matrixDB.cursor.rowcount)

    def delete_matrix(self, matrix_id):
        """
        Deletes the matrix from the database with the given ID

        Args:
            matrix_id (int): The ID of the matrix to be deleted
        """
        try:
            self.matrixDB.execute_query("DELETE FROM Matrix WHERE MatrixID=?", (matrix_id,))
            print(f"Matrix with ID {matrix_id} deleted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error deleting matrix:", e)

    def update_matrix(self, matrix_id, matrix):
        """
        Updates the matrix in the database with the given ID

        Args:
            matrix_id (int): The ID of the matrix to be updated
            matrix (Matrix): The updated matrix object
        """
        values = ' '.join([str(cell) for row in matrix for cell in row])
        rows = matrix.rows
        cols = matrix.cols

        try:
            self.matrixDB.execute_query("UPDATE Matrix SET _Rows=?, _Column=?, _Value=? WHERE MatrixID=?",
                                        (rows, cols, values, matrix_id))
            print(f"Matrix with ID {matrix_id} updated successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating matrix:", e)
        finally:
            print("Rows updated: ", self.matrixDB.cursor.rowcount)