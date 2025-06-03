from flask import Flask
import os

from Libraries.Connection import Connection
from Helpers.Helpers import Helpers

#=========== Configuración inicial de la aplicación
app = Flask(__name__, template_folder="Views", static_folder="Assets")
app.add_template_global(Helpers.url_files, name="url_files")
app.add_template_global(Helpers.url_base, name="url_base")

#=========== Importación de controladores
from Controllers.AuthController import AuthController
from Controllers.DashboardController import DashboardController
from Controllers.UsersController import UsersController
from Controllers.RolesController import RolesController
from Controllers.AudiosController import AudiosController
from Controllers.HomeController import HomeController

#=========== Registro de Blueprints
app.register_blueprint(HomeController().home_blueprint)
app.register_blueprint(DashboardController().dashboard_blueprint)
app.register_blueprint(AudiosController().audios_blueprint)
app.register_blueprint(AuthController().auth_blueprint, url_prefix="/auth")
app.register_blueprint(UsersController().users_blueprint, url_prefix="/users")
app.register_blueprint(RolesController().roles_blueprint)

#=========== Configuración de la clave secreta
app.secret_key = os.urandom(24)

#=========== Gestión del cierre de conexiones
@app.teardown_appcontext
def close_connection(exception):
    try:
        Connection.close()
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")

#=========== Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
