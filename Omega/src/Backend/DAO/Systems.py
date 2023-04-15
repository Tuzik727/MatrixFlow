from datetime import datetime

from Omega.src.Backend.MatrixDB import MatrixDB


class SystemsDAO:
    """
    This class provides methods to interact with the Systems table in the Matrix database.
    """

    def __init__(self, system_name: str, user_id: int):
        """
        Initializes a new instance of the SystemsDAO class.

        Args:
            system_name: A string representing the name of the system.
            user_id: An integer representing the user ID of the owner of the system.
        """
        self.system_name = system_name
        self.user_id = user_id
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor

    def insert_system(self):
        """
        Inserts a new system into the Systems table.

        Raises:
            Exception: An error occurred while inserting the system into the database.
        """
        try:
            self.matrixDB.execute_query(
                "INSERT INTO Systems(SystemName, UserID, DateCreated) "
                "VALUES (?, ?, ?)",
                (self.system_name, self.user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

            print("System inserted successfully. System ID: ", self.cursor.lastrowid)
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error inserting system:", e)
        finally:
            print("Rows inserted: ", self.cursor.rowcount)

    def delete_system(self, system_id: int):
        """
        Deletes a system from the Systems table.

        Args:
            system_id: An integer representing the ID of the system to delete.

        Raises:
            Exception: An error occurred while deleting the system from the database.
        """
        try:
            self.matrixDB.execute_query(
                "DELETE FROM Systems WHERE SystemID = ?",
                (system_id,))

            print("System deleted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error deleting system:", e)
        finally:
            print("Rows deleted: ", self.cursor.rowcount)

    def update_system(self, system_id: int, system_name: str):
        """
        Updates the name of a system in the Systems table.

        Args:
            system_id: An integer representing the ID of the system to update.
            system_name: A string representing the new name of the system.

        Raises:
            Exception: An error occurred while updating the system in the database.
        """
        try:
            self.matrixDB.execute_query(
                "UPDATE Systems SET SystemName = ? WHERE SystemID = ?",
                (system_name, system_id))

            print("System updated successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating system:", e)
        finally:
            print("Rows updated: ", self.cursor.rowcount)

    def getLastSystemID(self):
        """
        Gets the ID of the last system added to the Systems table.

        Returns:
            An integer representing the ID of the last system added to the Systems table.

        Raises:
            Exception: An error occurred while getting the ID of the last system from the database.
        """
        try:
            self.cursor.execute("SELECT TOP 1 SystemID FROM Systems ORDER BY SystemID DESC")
            ID = self.cursor.fetchone()
            return ID[0]
        except Exception as e:
            print("Error getting last system ID:", e)
