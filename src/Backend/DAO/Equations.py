from src.Backend.MatrixDB import MatrixDB
from src.MatrixOperation.LinearSystem.SolveSystem import get_equation_coeffs


class EquationDAO:
    """
    Data Access Object for Equation objects
    """

    def __init__(self, equation, system_id: int):
        """
        Initialize EquationDAO object with Equation object and System ID.

        :param equation: Equation object
        :param system_id: ID of the system to which this equation belongs
        """
        self.equation = equation
        self.system_id = system_id
        self.equation_str = str(equation)
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor

    def insert_equation(self):
        """
        Insert Equation into the database.
        """
        try:
            self.matrixDB.execute_query(
                "INSERT INTO Equations(SystemID, EquationString) VALUES (?, ?)",
                (self.system_id, self.equation_str)
            )
            print("Equation inserted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error inserting equation:", e)
        finally:
            print("Rows inserted: ", self.matrixDB.cursor.rowcount)

    def delete_equation(self, equation_id):
        """
        Delete Equation from the database.

        :param equation_id: ID of the Equation to be deleted
        """
        try:
            self.matrixDB.execute_query(
                "DELETE FROM Equations WHERE EquationID = ?",
                (equation_id,)
            )
            print("Equation deleted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error deleting equation:", e)
        finally:
            print("Rows deleted: ", self.matrixDB.cursor.rowcount)

    def update_equation(self, equation_id):
        """
        Update Equation in the database.

        :param equation_id: ID of the Equation to be updated
        """
        try:
            self.matrixDB.execute_query(
                "UPDATE Equations SET EquationString = ? WHERE EquationID = ?",
                (self.equation_str, equation_id)
            )
            print("Equation updated successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating equation:", e)
        finally:
            print("Rows updated: ", self.matrixDB.cursor.rowcount)
