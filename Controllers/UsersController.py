from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel

class UsersController:
    def __init__(self):
        self.users_blueprint = Blueprint('users', __name__)
        self.users_blueprint.add_url_rule('/', view_func=self.users)
        self.users_blueprint.add_url_rule('/profile', view_func=self.profile)

    def users(self):
        if 'userId' not in session:
                return redirect(url_for('auth.login'))

        user_id = session.get('userId')

        auth = AuthModel()
        user_data = auth.get_user_data(user_id)

        if not user_data:
            return redirect(url_for('auth.login'))

        if user_data['roleId'] != 1 or user_data['roleName'].lower() != 'admin':
            print("⚠️ Acceso denegado: rol cambiado o no autorizado.")
            session.clear()
            return redirect(url_for('auth.login'))

        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']

        print(f"✅ Acceso permitido para: {user_data['userName']} con rol {user_data['roleName']}")

        data = {
            "pageName": "users",
            "pageTitle": "Welcome To Users",
            "keywords": "users, panel",
            "description": "Users Admin"
        }

        return render_template("Users/users.html", data=data, user_data=user_data)

    def profile(self):
        if 'userId' not in session:
                return redirect(url_for('auth.login'))

        user_id = session.get('userId')

        auth = AuthModel()
        user_data = auth.get_user_data(user_id)

        if not user_data:
            return redirect(url_for('auth.login'))

        if user_data['roleId'] != 1 or user_data['roleName'].lower() != 'admin':
            print("⚠️ Acceso denegado: rol cambiado o no autorizado.")
            session.clear()
            return redirect(url_for('auth.login'))

        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']

        print(f"✅ Acceso permitido para: {user_data['userName']} con rol {user_data['roleName']}")

        data = {
            "pageName": "profile",
            "pageTitle": "Welcome To Profile",
            "keywords": "profile, panel",
            "description": "Profile Admin"
        }

        return render_template("Users/profile.html", data=data, user_data=user_data)