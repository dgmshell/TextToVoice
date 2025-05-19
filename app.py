from flask import Flask
app = Flask(__name__, template_folder="Views", static_folder="Assets")

from Controllers.AuthController import AuthController

auth_controller = AuthController()
app.register_blueprint(auth_controller.auth_blueprint,url_prefix="/auth")

if __name__ == '__main__':
         app.run(debug=True, host='0.0.0.0')