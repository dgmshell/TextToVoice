import mysql.connector
import os
from dotenv import load_dotenv

class Connection:
    _instance = None
    _cursor = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()

            try:
                cls._instance = mysql.connector.connect(
                    host=os.getenv('DB_HOST', 'localhost'),
                    user=os.getenv('DB_USER', 'root'),
                    password=os.getenv('DB_PASS', ''),
                    database=os.getenv('DB_NAME', 'insider')
                )
            except mysql.connector.Error as err:
                print(f"Error de conexión: {err}")
                cls._instance = None
        return cls._instance

    @staticmethod
    def get_cursor():
        if Connection._instance:
            if not Connection._cursor:
                Connection._cursor = Connection._instance.cursor(dictionary=True)
            return Connection._cursor
        raise Exception("Conexión no establecida")

    @staticmethod
    def close():
        if Connection._instance:
            if Connection._cursor:
                Connection._cursor.close()
            Connection._instance.close()
            Connection._instance = None
            Connection._cursor = None