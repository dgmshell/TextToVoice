from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel

class AuthController:
    def __init__(self):
        self.auth_blueprint = Blueprint('auth', __name__)
        self.auth_blueprint.add_url_rule('/login', view_func=self.login)
        self.auth_blueprint.add_url_rule('/signup', view_func=self.signup)
        self.auth_blueprint.add_url_rule('/recovery', view_func=self.recovery)
        self.auth_blueprint.add_url_rule('/logout', view_func=self.logout)
        self.auth_blueprint.add_url_rule('/setLogin', methods=['POST'], view_func=self.setLogin)
    def login(self):
        # Lógica para el login
        if 'roleId' in session and session.get('roleName') == 'admin':
                    return redirect(url_for('dashboard.dashboard'))
        data = {
                    "pageName": "login",
                    "pageTitle": "Welcome To Login",
                    "keywords": "login, auth",
                    "description": "Login "
                }
        return render_template('/Auth/login.html', data=data)
    def signup(self):
        # Lógica para el signup
        if 'roleId' in session and session.get('roleName') == 'admin':
                    return redirect(url_for('dashboard.dashboard'))
        data = {
                    "pageName": "signup",
                    "pageTitle": "Welcome To Signup",
                    "keywords": "signup, signup",
                    "description": "Signup "
                }
        return render_template('/Auth/signup.html', data=data)

    def setLogin(self):
            try:
                data = request.get_json()
                userEmail = data.get('userEmail')
                userPassword = data.get('userPassword')

                print(f"Datos recibidos: userEmail={userEmail}, userPassword={userPassword}")

                auth = AuthModel()
                result = auth.login(userEmail, userPassword)

                if result["status"] == "success":
                    user = result["user"]
                    session['userSession'] = result
                    session['userName'] = user['userName']
                    session['userId'] = user['userId']
                    session['roleId'] = user['roleId']
                    session['roleName'] = user['roleName']
                    return jsonify({"status": "login", "redirect": "yes"})
                else:
                    return jsonify(result)

            except Exception as e:
                print(f"Error en setLogin: {e}")
                return jsonify({"status": "error", "message": "Error interno del servidor"}), 500

    def logout(self):
         try:
             session.clear()
             return redirect(url_for('auth.login'))

         except Exception as e:
              print(f"Error al cerrar la conexion: {e}")
    def recovery(self):
            # Lógica para el signup
            if 'roleId' in session and session.get('roleName') == 'admin':
                        return redirect(url_for('dashboard.dashboard'))
            data = {
                        "pageName": "recovery",
                        "pageTitle": "Welcome To Recovery",
                        "keywords": "recovery, recovery",
                        "description": "Recovery "
                    }
            return render_template('/Auth/recovery.html', data=data)
