from flask import Blueprint, render_template, session, request, jsonify, redirect, url_for
from Models.UsersModel import UsersModel
from Models.AuthModel import AuthModel

class UsersController:
    def __init__(self):
        self.users_blueprint = Blueprint('users', __name__)
        self.users_blueprint.add_url_rule('/', view_func=self.users)
        self.users_blueprint.add_url_rule('/profile', view_func=self.profile)
        self.users_blueprint.add_url_rule('/setProfile', methods=['POST'], view_func=self.setProfile)
        self.users_blueprint.add_url_rule('/deleteUserId', methods=['POST'], view_func=self.deleteUserId)

    def users(self):
        if 'userId' not in session:
            return redirect(url_for('auth.login'))

        user_id = session.get('userId')

        auth = AuthModel()
        user_data = auth.get_user_data(user_id)

        users = UsersModel()
        users_details = users.get_all_users()

        if not user_data:
            return redirect(url_for('auth.login'))

        if user_data['roleId'] != 1 or user_data['roleName'].lower() != 'admin':
            print("⚠️ Acceso denegado: rol cambiado o no autorizado.")
            session.clear()
            return redirect(url_for('users.profile'))

        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']



        return render_template("Users/users.html", users=users_details, user_data=user_data)

    def profile(self):
        if 'userId' not in session:
            return redirect(url_for('auth.login'))

        user_id = session.get('userId')

        users = AuthModel()
        user_data = users.get_user_data(user_id)

        if not user_data:
            return redirect(url_for('auth.login'))


        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']


        return render_template("Users/profile.html",  user_data=user_data)

    def setProfile(self):
        try:
            data = request.get_json()
            profileNames = data.get('profileNames')
            profileSurnames = data.get('profileSurnames')
            profileEmail = data.get('profileEmail')
            userName = data.get('userName')
            userPassword = data.get('userPassword')
            user_id = session.get('userId')
            print("userPassword: ", userPassword)
            users = UsersModel()
            response = users.update(user_id, profileNames, profileSurnames, profileEmail, userName, userPassword)

            if response["status"] == "success":
               return jsonify({"status": "update", "redirect": "yes","message":"Perfil actualizado...espera una segundos"})

        except Exception as e:
            print(f"Error en setProfile: {e}")
            return jsonify({"message": "Error interno del servidor."}), 500

    def deleteUserId(self):
        try:
            data = request.get_json()
            userId = data.get('userId2')

            users = UsersModel()
            response = users.delete(userId)

            return jsonify(response)

        except Exception as e:
            print(f"Error en deleteUserId: {e}")
            return jsonify({"message": "Error interno del servidor."}), 500
