import mysql.connector
import bcrypt
from Libraries.Connection import Connection
class AuthModel:
    def __init__(self):
        try:
            _ = Connection()
            self.cursor = Connection.get_cursor()
            self.connection = Connection._instance
        except Exception as e:
            print(f"Error al obtener el cursor: {e}")
            self.cursor = None
            self.connection = None

    def login(self, email, password):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:

            self.cursor.execute("""
                SELECT
                    u.userId, u.userName, u.userPassword,
                    r.roleId, r.roleName, r.roleDescription
                FROM users u
                LEFT JOIN roles r ON u.roleId = r.roleId
                WHERE u.userName = %s
                LIMIT 1
            """, (email,))
            user = self.cursor.fetchone()

            if user:
                stored_password_hash = user.get('userPassword')

                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    user.pop('userPassword', None)  # Limpiar contraseña
                    return {
                        "status": "success",
                        "user": user
                    }


            return {
                "status": "error",
                "message": "Credenciales incorrectas"
            }

        except mysql.connector.Error as e:
            return {
                "status": "error",
                "message": "Error al procesar la solicitud"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": "Error interno en el servidor"
            }