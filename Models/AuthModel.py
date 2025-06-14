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

    def get_user_data(self, user_id):
        if not self.cursor:
            return None
        try:
            self.cursor.execute("""
                SELECT
                    u.userId,
                    u.userName,
                    u.roleId,
                    r.roleName,
                    p.profileNames,
                    p.profileSurnames,
                    p.profileEmail
                FROM users u
                INNER JOIN roles r ON u.roleId = r.roleId
                INNER JOIN profiles p ON u.userId = p.userId
                WHERE u.userId = %s
            """, (user_id,))

            user_data = self.cursor.fetchone()
            return user_data

        except Exception as e:
            print(f"Error al obtener los datos del usuario: {e}")
            return None

    def signup(self, profileNames, profileSurnames, profileEmail, userName, userPassword):
        roleId = 1  # Rol por defecto

        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            # Verificar si el nombre de usuario ya existe
            self.cursor.execute("SELECT * FROM users WHERE userName = %s", (userName,))
            if self.cursor.fetchone():
                return {
                    "status": "error",
                    "message": "El nombre de usuario ya está registrado"
                }

            # Verificar si el correo ya existe
            self.cursor.execute("SELECT * FROM profiles WHERE profileEmail = %s", (profileEmail,))
            if self.cursor.fetchone():
                return {
                    "status": "error",
                    "message": "El correo ya está registrado"
                }

            # Encriptar la contraseña
            hashed_password = bcrypt.hashpw(userPassword.encode('utf-8'), bcrypt.gensalt())

            # Insertar en users
            self.cursor.execute("""
                INSERT INTO users (userName, userPassword, roleId)
                VALUES (%s, %s, %s)
            """, (userName, hashed_password.decode('utf-8'), roleId))
            self.connection.commit()

            # Obtener el userId insertado
            user_id = self.cursor.lastrowid

            # Insertar en profiles
            self.cursor.execute("""
                INSERT INTO profiles (userId, profileNames, profileSurnames, profileEmail)
                VALUES (%s, %s, %s, %s)
            """, (user_id, profileNames, profileSurnames, profileEmail))
            self.connection.commit()

            return {
                "status": "success",
                "message": "Usuario registrado con éxito"
            }

        except mysql.connector.Error as e:
            return {
                "status": "error",
                "message": f"Error en la consulta MySQL: {e}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error inesperado: {e}"
            }
