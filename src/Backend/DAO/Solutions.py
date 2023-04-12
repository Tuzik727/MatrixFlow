from src.Backend.MatrixDB import MatrixDB


class SolutionDAO:
    def __init__(self, system_id: int, solution_string: str):
        """
        A class to represent a solution data access object.

        Parameters:
        system_id (int): The ID of the system associated with the solution.
        solution_string (str): A string representation of the solution.

        Attributes:
        system_id (int): The ID of the system associated with the solution.
        solution_string (str): A string representation of the solution.
        matrixDB (MatrixDB): An instance of the MatrixDB class for database operations.
        cursor: A cursor object for executing SQL queries.

        """
        self.system_id = system_id
        self.solution_string = solution_string
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor

    def insert_solution(self):
        """
        Inserts a solution into the Solutions table in the database.

        Returns:
        None

        """
        try:
            self.matrixDB.execute_query(
                "INSERT INTO Solutions(SystemID, SolutionString) "
                "VALUES (?, ?)",
                (self.system_id, self.solution_string))
            print("Solution inserted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error inserting solution:", e)
        finally:
            print("Rows inserted: ", self.matrixDB.cursor.rowcount)

    def delete_solution(self, solution_id: int):
        """
        Deletes a solution from the Solutions table in the database.

        Parameters:
        solution_id (int): The ID of the solution to be deleted.

        Returns:
        None

        """
        try:
            self.matrixDB.execute_query(
                "DELETE FROM Solutions WHERE SolutionID = ?", (solution_id,))
            print("Solution deleted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error deleting solution:", e)
        finally:
            print("Rows affected: ", self.matrixDB.cursor.rowcount)

    def update_solution(self, solution_id: int, solution_string: str):
        """
        Updates a solution in the Solutions table in the database.

        Parameters:
        solution_id (int): The ID of the solution to be updated.
        solution_string (str): The new string representation of the solution.

        Returns:
        None

        """
        try:
            self.matrixDB.execute_query(
                "UPDATE Solutions SET SolutionString = ? WHERE SolutionID = ?",
                (solution_string, solution_id))
            print("Solution updated successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating solution:", e)
        finally:
            print("Rows affected: ", self.matrixDB.cursor.rowcount)