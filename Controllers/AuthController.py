from flask import Blueprint, render_template
class AuthController:
    def __init__(self):
        self.auth_blueprint = Blueprint('auth', __name__)
        self.auth_blueprint.add_url_rule('/login', view_func=self.login)
        self.auth_blueprint.add_url_rule('/setLogin', methods=['POST'], view_func=self.setLogin)
    def login(self):
        # Lógica para el login
        return render_template('/Auth/login.html')

    def setLogin(self):
      data = {
          "pageName": "login",
          "pageTitle": "Welcome To Login",
          "keywords": "login, auth",
          "description": "Login"
      }
      return data
