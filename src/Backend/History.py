import pyodbc

from src.Backend.DAO.Matrix import MatrixDAO
from src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from src.Backend.DAO.Solutions import SolutionDAO
from src.Backend.DAO.Systems import SystemsDAO
from src.Backend.DAO.Equations import EquationDAO
from src.Backend.MatrixDB import MatrixDB


class History:
    """ A class to represent the history of matrices.
    Attributes:
    - matrix: a MatrixDAO object
    - system: a SystemsDAO object
    - calcMatrix: a CalculatedMatrixDAO object
    - equation: an EquationDAO object
    - solution: a SolutionDAO object
    - matrixDB: a MatrixDB object for database connection
    - cursor: a cursor for executing SQL statements
    """

    def __init__(self):
        """
        Initializes a new instance of the History class.
        """
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor

    def getMatrixDataByUser(self, userID):
        """
        Retrieves all matrices owned by a user from the database and returns them as a dictionary.

        Args:
        - userID: an int representing the ID of the user.

        Returns:
        - A dictionary containing the matrix data. Each key represents a matrix ID and the corresponding value is another
        dictionary containing the matrix's attributes such as its number of rows, columns, values, the ID of its owner, and its creation date.
        """
        try:
            self.cursor.execute("SELECT * FROM Matrix WHERE UserID = ?", userID)
            rows = self.cursor.fetchall()
            data_dict = {}
            for row in rows:
                data_dict[row[0]] = {
                    '_Rows': row[1],
                    '_Column': row[2],
                    '_value': row[3],
                    'UserID': row[4],
                    'DateCreated': row[5]
                }
            return data_dict
        except pyodbc.Error as e:
            print('Error retrieving matrix data:', e)
            raise
        finally:
            self.matrixDB.disconnect()

    def getCalcMatrixDataByUser(self, userID):
        """
        Retrieves calculated matrix data for a given user.

        Args:
            userID (int): The ID of the user.

        Returns:
            dict: A dictionary containing the calculated matrix data for the user.

        Raises:
            pyodbc.Error: If there is an error retrieving the data from the database.
        """
        try:
            self.cursor.execute("SELECT CalculatedMatrix.CalculatedMatrixID, CalculatedMatrix._Rows, "
                                "CalculatedMatrix._Column, CalculatedMatrix._Value, CalculatedMatrix.MatrixOperation, "
                                "CalculatedMatrix.matrixID, CalculatedMatrix.DateCreated, Matrix.UserID FROM "
                                "CalculatedMatrix inner join Matrix on CalculatedMatrix.matrixID = Matrix.MatrixID WHERE "
                                "Matrix.UserID = ?", userID)
            rows = self.cursor.fetchall()
            data_dict = {}
            for row in rows:
                data_dict[row[0]] = {
                    'Rows': row[1],
                    'Column': row[2],
                    'Value': row[3],
                    'Operation': row[4],
                    'MatrixID': row[5],
                    'DateCreated': row[6],
                    'UserID': row[7]
                }
            return data_dict
        except pyodbc.Error as e:
            print("Error retrieving calculated matrix data:", e)
            raise

    def getSystemDataByUser(self, userID):
        """
        Retrieves all system data for a given user from the Systems table in the database.

        Args:
            userID (int): The user ID to retrieve system data for.

        Returns:
            dict: A dictionary containing system data for the user, where the keys are the system IDs and the values are
            dictionaries containing the system name, date created, and user ID.

        Raises:
            pyodbc.Error: If there is an error executing the SQL query.
        """
        try:
            self.cursor.execute("SELECT * FROM Systems WHERE UserID = ?", userID)
            rows = self.cursor.fetchall()
            data_dict = {}
            for row in rows:
                data_dict[row[0]] = {
                    'SystemName': row[1],
                    'DateCreated': row[2],
                    'UserID': row[3],
                }
            return data_dict
        except pyodbc.Error as e:
            print('Error retrieving system data:', e)
            raise

    def getEquationDataByUserSystem(self, userID, systemID):
        """
        Retrieves equation data for a specific user and system.

        Args:
            userID (int): the ID of the user whose equation data is being retrieved.
            systemID (int): the ID of the system whose equation data is being retrieved.

        Returns:
            dict: a dictionary containing equation data for the specified user and system, with equation IDs as keys.

        Raises:
            pyodbc.Error: if there is an error retrieving equation data from the database.
        """
        try:
            self.cursor.execute("SELECT Equations.EquationID, Equations.SystemID, Equations.EquationString "
                                "FROM Equations INNER JOIN Systems ON Equations.SystemID = Systems.SystemID "
                                "WHERE Systems.UserID = ? AND Equations.SystemID = ?", userID, systemID)
            rows = self.cursor.fetchall()
            data_dict = {}
            for row in rows:
                data_dict[row[0]] = {
                    'SystemID': row[1],
                    'EquationString': row[2],
                }
            return data_dict
        except pyodbc.Error as e:
            print("Error retrieving equation data:", e)
            raise

    def getSolutionDataByUserSystem(self, userID, systemID):
        """
        Retrieves solution data for a specific user and system.

        Args:
            userID (int): The ID of the user.
            systemID (int): The ID of the system.

        Returns:
            dict: A dictionary containing the solution data for the specified user and system, where the keys are
            the solution IDs and the values are dictionaries with 'SystemID' and 'SolutionString' keys.

        Raises:
            pyodbc.Error: If there is an error retrieving the solution data from the database.
        """
        try:
            self.cursor.execute("Select Solutions.SolutionID, Solutions.SystemID, Solutions.SolutionString "
                                "From Solutions inner join Systems on Solutions.SystemID = Systems.SystemID "
                                "WHERE Systems.UserID = ? and Solutions.SystemID = ?", userID, systemID)
            rows = self.cursor.fetchall()
            data_dict = {}
            for row in rows:
                data_dict[row[0]] = {
                    'SystemID': row[1],
                    'SolutionString': row[2],
                }
            return data_dict
        except pyodbc.Error as e:
            print("Error retrieving solution data:", e)
            raise

    def getSystemsIDbyUser(self, userID):
        """
        Retrieve system IDs associated with the given user ID from the database.

        Args:
        - userID (int): User ID to retrieve system IDs for.

        Returns:
        - list of tuples: List of tuples where each tuple contains a system ID.
        """
        try:
            self.cursor.execute("SELECT SystemID FROM Systems WHERE UserID = ?", userID)
            ids = self.cursor.fetchall()
            return ids
        except pyodbc.Error as e:
            print("Error retrieving system IDs for user:", e)
            raise

    def linearSystemHistory(self, userID):
        """
        Retrieve linear system history associated with the given user ID.

        Args:
        - userID (int): User ID to retrieve linear system history for.

        Returns:
        - tuple: A tuple containing three elements:
            - systems (dict): A dictionary of system data associated with the given user ID.
            - equations (list): A list of dictionaries where each dictionary contains equation data associated with a system ID.
            - solutions (list): A list of dictionaries where each dictionary contains solution data associated with a system ID.
        """
        systems = self.getSystemDataByUser(userID)
        systemsIds = self.getSystemsIDbyUser(userID)
        systemsIds = [ids[0] for ids in systemsIds]
        equations = []
        solutions = []
        for i in systemsIds:
            equations.append(self.getEquationDataByUserSystem(userID, i))
            solutions.append(self.getSolutionDataByUserSystem(userID, i))

        return systems, equations, solutions