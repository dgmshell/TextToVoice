from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
class DashboardController:
    def __init__(self):
        self.dashboard_blueprint = Blueprint('dashboard', __name__)
        self.dashboard_blueprint.add_url_rule('/dashboard', view_func=self.dashboard)

    def dashboard(self):
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
            "pageName": "dashboard",
            "pageTitle": "Welcome To Dashboard",
            "keywords": "dashboard, panel",
            "description": "Dashboard Admin"
        }

        return render_template("Dashboard/dashboard.html", data=data, user_data=user_data)
