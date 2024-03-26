import pyodbc
from db_property_util import DBPropertyUtil
# from DatabaseConnectionHandling import DatabaseConnectionError
class DBConnUtil:
    def get_connection():
        try:
            connection_string = DBPropertyUtil.get_connection_string()
            connection = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return connection

        except pyodbc.Error  as e:
            raise DatabaseConnectionError("Error connecting to the database:", e)
