import mysql.connector
import bcrypt
from Libraries.Connection import Connection

class ConverterModel:
    def __init__(self):
        try:
            _ = Connection()
            self.cursor = Connection.get_cursor()
            self.connection = Connection._instance
        except Exception as e:
            print(f"Error al obtener el cursor: {e}")
            self.cursor = None
            self.connection = None

    def save(self, userId, audioIdFile, audioTitle, audioText, audioLanguage):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            # Verificar si ya existe un audio con el mismo título para el mismo usuario
            self.cursor.execute("""
                SELECT * FROM audios WHERE userId = %s AND audioTitle = %s
            """, (userId, audioTitle))

            if self.cursor.fetchone():
                return {
                    "status": "exists",
                    "message": "Ya existe un audio con ese título. Elige otro título."
                }

            # Insertar nuevo audio
            self.cursor.execute("""
                INSERT INTO audios (userId, audioIdFile, audioTitle, audioText, audioLanguage)
                VALUES (%s, %s, %s, %s, %s)
            """, (userId, audioIdFile, audioTitle, audioText, audioLanguage))

            self.connection.commit()

            return {
                "status": "successSave",
                "message": "Audio guardado exitosamente"
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
    def get_all_audios(self):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            self.cursor.execute("""
                SELECT
                    a.audioId,
                    a.audioIdFile,
                    a.audioTitle,
                    a.audioText,
                    a.audioLanguage,
                    a.userId,
                    u.userName,
                    a.createdAt,
                    CASE
                        WHEN f.favoriteId IS NOT NULL THEN 1
                        ELSE 0
                    END AS isFavorite
                FROM audios a
                JOIN users u ON a.userId = u.userId
                LEFT JOIN favorites f ON a.audioId = f.audioId
                ORDER BY a.createdAt DESC
            """)

            rows = self.cursor.fetchall()

            return rows

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


    def get_all_by_user(self, userId):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:
            self.cursor.execute("""
                SELECT a.audioId, a.audioIdFile, a.audioTitle, a.audioText, a.audioLanguage, a.createdAt, u.userName
                FROM audios a
                JOIN users u ON a.userId = u.userId
                WHERE a.userId = %s
                ORDER BY a.createdAt DESC
            """, (userId,))

            rows = self.cursor.fetchall()

            return rows

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
    def delete(self, audioId):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:

            # Primero eliminar de favoritos (si existe)
            self.cursor.execute("""
                DELETE FROM favorites
                WHERE audioId = %s
            """, (audioId,))

            # Luego eliminar el audio
            self.cursor.execute("""
                DELETE FROM audios
                WHERE audioId = %s
            """, (audioId,))

            self.connection.commit()

            return {
                "status": "success",
                "message": "Audio y sus favoritos eliminados correctamente"
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

    def add(self, userId, audioId):
        if not self.cursor or not self.connection:
            return {
                "status": "error",
                "message": "No se pudo establecer conexión con la base de datos"
            }

        try:

            self.cursor.execute("""
                SELECT statusFavorite FROM favorites WHERE userId = %s AND audioId = %s
            """, (userId, audioId))

            row = self.cursor.fetchone()

            if row is not None:
                current_status = row['statusFavorite'] if isinstance(row, dict) else row[0]
                new_status = 0 if current_status == 1 else 1

                self.cursor.execute("""
                    UPDATE favorites SET statusFavorite = %s WHERE userId = %s AND audioId = %s
                """, (new_status, userId, audioId))

                self.connection.commit()

                return {
                    "status": "success",
                    "statusFavorite": new_status,
                    "message": "Estado favorito actualizado correctamente"
                }

            else:
                # Insertar nuevo favorito con statusFavorite = 1
                print("[DEBUG] Insertando nuevo favorito con statusFavorite = 1")
                self.cursor.execute("""
                    INSERT INTO favorites (userId, audioId, statusFavorite)
                    VALUES (%s, %s, 1)
                """, (userId, audioId))

                self.connection.commit()

                return {
                    "status": "successSave",
                    "statusFavorite": 1,
                    "message": "Favorito guardado exitosamente"
                }

        except mysql.connector.Error as e:
            print(f"[ERROR MYSQL] {e}")
            return {
                "status": "error",
                "message": f"Error en la consulta MySQL: {e}"
            }
        except Exception as e:
            print(f"[ERROR EXCEPCIÓN] {e}")
            return {
                "status": "error",
                "message": f"Error inesperado: {e}"
            }

