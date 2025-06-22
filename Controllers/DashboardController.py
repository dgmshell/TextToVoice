from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
from Models.ConverterModel import ConverterModel
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

        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']


            converter = ConverterModel()
            audios = converter.get_all_audios()



        return render_template("Dashboard/dashboard.html",audios = audios,  user_data=user_data)
