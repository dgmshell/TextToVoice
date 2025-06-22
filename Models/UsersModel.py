import mysql.connector
import bcrypt
from Libraries.Connection import Connection

class UsersModel:
    def __init__(self):
        try:
            _ = Connection()
            self.cursor = Connection.get_cursor()
            self.connection = Connection._instance
        except Exception as e:
            print(f"Error al obtener el cursor: {e}")
            self.cursor = None
            self.connection = None

    def update(self, user_id, profileNames, profileSurnames, profileEmail, userName, userPassword):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            # Verificar si otro usuario ya tiene ese nombre de usuario
            self.cursor.execute("""
                SELECT * FROM users
                WHERE userName = %s AND userId != %s
            """, (userName, user_id))
            if self.cursor.fetchone():
                return {
                    "status": "error",
                    "message": "El nombre de usuario ya está en uso por otro usuario"
                }

            # Verificar si otro perfil ya tiene ese correo
            self.cursor.execute("""
                SELECT * FROM profiles
                WHERE profileEmail = %s AND userId != %s
            """, (profileEmail, user_id))
            if self.cursor.fetchone():
                return {
                    "status": "error",
                    "message": "El correo ya está en uso por otro perfil"
                }

            # Actualizar tabla users
            if userPassword:  # Solo si se proporcionó una nueva contraseña
                hashed_password = bcrypt.hashpw(userPassword.encode('utf-8'), bcrypt.gensalt())
                self.cursor.execute("""
                    UPDATE users
                    SET userName = %s, userPassword = %s
                    WHERE userId = %s
                """, (userName, hashed_password.decode('utf-8'), user_id))
            else:
                self.cursor.execute("""
                    UPDATE users
                    SET userName = %s
                    WHERE userId = %s
                """, (userName, user_id))

            # Actualizar tabla profiles
            self.cursor.execute("""
                UPDATE profiles
                SET profileNames = %s, profileSurnames = %s, profileEmail = %s
                WHERE userId = %s
            """, (profileNames, profileSurnames, profileEmail, user_id))

            self.connection.commit()

            return {
                "status": "success",
                "message": "Usuario actualizado con éxito"
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

    def get_all_users(self):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            self.cursor.execute("""
                SELECT
                    u.userId,
                    u.userName,
                    u.roleId,
                    r.roleName,
                    p.profileNames,
                    p.profileSurnames,
                    p.profileEmail,
                    u.create_at
                FROM users u
                INNER JOIN profiles p ON u.userId = p.userId
                INNER JOIN roles r ON u.roleId = r.roleId
            """)

            users = self.cursor.fetchall()  # Asumiendo cursor configurado con dictionary=True

            return users

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

    def delete(self, userId):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            print(f"[DEBUG] Eliminando perfil de userId: {userId}")
            self.cursor.execute("""
                DELETE FROM profiles
                WHERE userId = %s
            """, (userId,))

            print(f"[DEBUG] Eliminando usuario userId: {userId}")
            self.cursor.execute("""
                DELETE FROM users
                WHERE userId = %s
            """, (userId,))

            self.connection.commit()

            return {
                "status": "success",
                "message": "Usuario y perfil eliminados correctamente"
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