from src.Backend.MatrixDB import MatrixDB


class UserDAO:
    """
    Data Access Object class for handling user data in the database.
    """

    def __init__(self):
        """
        Constructor method for UserDAO class.
        Initializes instance variables and establishes connection with MatrixDB.
        """
        self.username = None
        self.password = None
        self.email = None
        self.date_created = None
        self.matrixDB = MatrixDB()
        self.cursor = self.matrixDB.cursor
        self.logged = False

    def insert_user(self, username: str, password: str, email: str, date_created):
        """
        Inserts a new user into the database.

        :param username: The username of the new user.
        :param password: The password of the new user.
        :param email: The email address of the new user.
        :param date_created: The date the user was created.
        """
        self.username = username
        self.password = password
        self.email = email
        self.date_created = date_created
        try:
            self.matrixDB.execute_query(
                "INSERT INTO Users(UserName, Password, Email, DateCreated) "
                "VALUES (?, ?, ?, ?)",
                (self.username, self.password, self.email, self.date_created))
            print("User inserted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error inserting user:", e)
        finally:
            print("Rows inserted: ", self.matrixDB.cursor.rowcount)

    def delete_user(self, user_id: int):
        """
        Deletes a user from the database.

        :param user_id: The ID of the user to be deleted.
        """
        try:
            self.matrixDB.execute_query(
                "DELETE FROM Users WHERE UserID = ?",
                (user_id,))
            print("User deleted successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error deleting user:", e)
        finally:
            print("Rows deleted: ", self.matrixDB.cursor.rowcount)

    def update_user(self, user_id: int, new_username: str, new_password: str, new_email: str):
        """
        Updates a user in the database.

        :param user_id: The ID of the user to be updated.
        :param new_username: The new username for the user.
        :param new_password: The new password for the user.
        :param new_email: The new email address for the user.
        """
        try:
            self.matrixDB.execute_query(
                "UPDATE Users SET UserName = ?, Password = ?, Email = ? WHERE UserID = ?",
                (new_username, new_password, new_email, user_id))
            print("User updated successfully.")
        except Exception as e:
            self.matrixDB.conn.rollback()
            print("Error updating user:", e)
        finally:
            print("Rows updated: ", self.matrixDB.cursor.rowcount)

    def get_user_by_username(self, username):
        """
        Retrieves a user from the database by their username.

        :param username: The username of the user to retrieve.
        :return: True if the user was found, False otherwise.
        """
        try:
            self.cursor.execute(
                "SELECT * FROM Users WHERE UserName = ?",
                (username,))
            row = self.cursor.fetchone()
            if row is not None:
                self.username = row[1]
                self.password = row[2]
                self.email = row[3]
                self.date_created = row[4]
                return True
        except Exception as e:
            print("Error getting user by username:", e)

    def get(self, userID):
        """
        Retrieves user information from the database using their user ID.

        Args:
        - userID (int): the ID of the user to retrieve

        Returns:
        - True if the user was found and their information was successfully retrieved, or False otherwise

        Raises:
        - Exception: if an error occurs while retrieving the user information
        """
        try:
            self.cursor.execute(
                "SELECT * FROM Users WHERE UserID = ?",
                userID, )
            row = self.cursor.fetchone()
            if row is not None:
                self.username = row[0]
                self.password = row[1]
                self.email = row[2]
                self.date_created = row[3]
                return True
        except Exception as e:
            print("Error getting user by ID:", e)

    def check_password(self, password):
        """
        Checks if the given password matches the user's password.

        Args:
        - password (str): the password to check

        Returns:
        - True if the password matches the user's password, or False otherwise
        """
        return password == self.password

    def get_userID(self):
        """
        Retrieves the user ID from the database using the user's username.

        Returns:
        - The user ID (int) if the username was found, or None otherwise
        """
        self.cursor.execute("SELECT UserID FROM Users WHERE UserName = ?", (self.username,))
        ID = self.cursor.fetchone()
        print(ID[0])
        return ID[0]

    def get_user_by_email(self, email):
        """
        Retrieves user information from the database using their email address.

        Args:
        - email (str): the email address of the user to retrieve

        Returns:
        - True if the user was found and their information was successfully retrieved, or False otherwise

        Raises:
        - Exception: if an error occurs while retrieving the user information
        """
        try:
            self.cursor.execute(
                "SELECT * FROM Users WHERE Email = ?",
                (email,))
            row = self.cursor.fetchone()
            if row is not None:
                self.username = row[1]
                self.password = row[2]
                self.email = row[3]
                self.date_created = row[4]
                return True
        except Exception as e:
            print("Error getting user by email:", e)