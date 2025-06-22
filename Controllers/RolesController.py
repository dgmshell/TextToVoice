from flask import Blueprint, render_template, session, request, jsonify, redirect, url_for
from Models.AuthModel import AuthModel
from Models.RolesModel import RolesModel

class RolesController:
    def __init__(self):
        self.roles_blueprint = Blueprint('roles', __name__)
        self.roles_blueprint.add_url_rule('/', view_func=self.roles)
        self.roles_blueprint.add_url_rule('/roles', view_func=self.roles)
        self.roles_blueprint.add_url_rule('/setRoleId', methods=['POST'], view_func=self.setRoleId)

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


        return render_template("Roles/roles.html", user_data=user_data)

    def setRoleId(self):
        try:
            data = request.get_json()

            roleId = data.get('roleId')
            userId = data.get('userId')

            roles = RolesModel()
            response = roles.update(userId, roleId)

            if response["status"] == "success":
                return jsonify({
                    "status": "update",
                    "redirect": "yes",
                    "message": "Rol actualizado... espera unos segundos"
                })
            else:
                return jsonify(response)

        except Exception as e:
            print(f"Error en setRoleId: {e}")
            return jsonify({"message": "Error interno del servidor."}), 500
