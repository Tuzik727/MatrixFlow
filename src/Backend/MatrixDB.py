import pyodbc

from src.MatrixOperation.Matrix import Matrix


class MatrixDB:
    DRIVER = 'Driver={SQL Server};'
    SERVER = 'SERVER=193.85.203.188;'
    DATABASE = 'DATABASE=butym;'
    USERNAME = 'UID=butym;'
    PASSWORD = 'PWD=7z124aow'

    def __init__(self):
        """
        Initializes the MatrixDB object by establishing a connection to the database.
        """
        try:
            self.conn = pyodbc.connect(self.DRIVER + self.SERVER + self.DATABASE + self.USERNAME + self.PASSWORD)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print('Error connecting to the database:', e)
            raise

    def disconnect(self):
        """
        Disconnects from the database.
        """
        try:
            if self.conn:
                self.conn.close()
                print('Connection to database closed')
            else:
                print('No active database connection')
        except pyodbc.Error as e:
            print('Error disconnecting from the database:', e)
            raise

    def execute_query(self, query: str, params=None):
        """
        Executes the given SQL query with optional parameters.

        Args:
            query (str): SQL query to execute.
            params (list): List of parameters to pass into the query. Defaults to None.

        Raises:
            pyodbc.Error: If there is an error executing the query.

        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print('Query executed successfully')
        except pyodbc.Error as e:
            self.conn.rollback()
            print('Error executing query:', e)
            raise

    def fetch_all(self):
        """
        Fetches all rows from the result set.

        Returns:
            List: List of tuples containing all rows from the result set.

        """
        try:
            rows = self.cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print('Error fetching all rows:', e)
            raise

    def fetch_one(self):
        """
        Fetches a single row from the result set.

        Returns:
            Tuple: Tuple containing a single row from the result set.

        """
        try:
            row = self.cursor.fetchone()
            return row
        except pyodbc.Error as e:
            print('Error fetching a single row:', e)
            raise

    def insert_matrix(self, UserID, matrix):
        """
        Inserts a matrix into the Matrix table of the database.

        Args:
            UserID (int): The ID of the user who owns the matrix.
            matrix (Matrix): The matrix to insert into the database.

        Raises:
            Exception: If an error occurs while inserting the matrix into the database.

        Returns:
            None
        """
        try:
            # Retrieve the last inserted matrix ID
            self.cursor.execute("SELECT TOP 1 MatrixID FROM Matrix ORDER BY MatrixID DESC")
            row = self.cursor.fetchone()
            matrix_id = row[0] if row else None

            # Insert the matrix values into the MatrixValue table
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    self.cursor.execute(
                        "INSERT INTO Matrix(UserID, _Rows, _Column, _Value) VALUES (?, ?, ?, ?)",
                        (UserID, i, j, matrix[i, j]))
            self.conn.commit()
            print("Matrix inserted successfully. Matrix ID: ", matrix_id)
        except pyodbc.Error as e:
            self.conn.rollback()
            print("Error inserting matrix:", e)
            raise
        except Exception as e:
            self.conn.rollback()
            print("Unexpected error occurred while inserting matrix:", e)
            raise
        finally:
            print("Rows inserted: ", self.cursor.rowcount)

    def insert_calculated_matrix(self, matrix, operation):
        try:
            # Retrieve the last inserted matrix ID
            self.cursor.execute(
                "SELECT TOP 1 CalculatedMatrixID FROM CalculatedMatrix ORDER BY CalculatedMatrixID DESC")
            row = self.cursor.fetchone()
            matrix_id = row[0] if row else 0

            # Insert the matrix values into the MatrixValue table
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    self.cursor.execute(
                        "INSERT INTO CalculatedMatrix(_Rows, _Column, _Value, MatrixOperation) VALUES (?, ?, "
                        "?, ?)",
                        (i, j, matrix[i, j], operation))
            self.conn.commit()
            print("Matrix inserted successfully. Calculated Matrix ID: ", matrix_id)
        except Exception as e:
            self.conn.rollback()
            print("Error inserting matrix:", e)
        finally:
            print("Rows inserted: ", self.cursor.rowcount)
