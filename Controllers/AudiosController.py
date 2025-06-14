from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
class AudiosController:
    def __init__(self):
        self.audios_blueprint = Blueprint('audios', __name__)
        self.audios_blueprint.add_url_rule('/audios', view_func=self.audios)

    def audios(self):
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
            "pageName": "audios",
            "pageTitle": "Welcome To Users",
            "keywords": "audios, panel",
            "description": "Users Admin"
        }

        return render_template("Audios/audios.html", data=data, user_data=user_data)