from flask import Flask
import os

from Libraries.Connection import Connection
from Helpers.Helpers import Helpers

app = Flask(__name__, template_folder="Views", static_folder="Assets")
app.add_template_global(Helpers.url_files, name="url_files")
app.add_template_global(Helpers.url_base, name="url_base")

from Controllers.AuthController import AuthController
from Controllers.DashboardController import DashboardController
from Controllers.HomeController import HomeController



home_controller = HomeController()
app.register_blueprint(home_controller.home_blueprint)

dashboard_controller = DashboardController()
app.register_blueprint(dashboard_controller.dashboard_blueprint)

auth_controller = AuthController()
app.register_blueprint(auth_controller.auth_blueprint,url_prefix="/auth")

app.secret_key = os.urandom(24)
@app.teardown_appcontext
def close_connection(exception):
    try:
        Connection.close()
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")
if __name__ == '__main__':
         app.run(debug=True, host='0.0.0.0')