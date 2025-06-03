from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
class RolesController:
    def __init__(self):
        self.roles_blueprint = Blueprint('roles', __name__)
        self.roles_blueprint.add_url_rule('/roles', view_func=self.roles)

    def roles(self):
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
            "pageName": "roles",
            "pageTitle": "Welcome To roles",
            "keywords": "roles, panel",
            "description": "Dashboard Admin"
        }

        return render_template("Roles/roles.html", data=data, user_data=user_data)
