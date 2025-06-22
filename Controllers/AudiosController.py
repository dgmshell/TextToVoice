from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
from Models.ConverterModel import ConverterModel
class AudiosController:
    def __init__(self):
        self.audios_blueprint = Blueprint('audios', __name__)
        self.audios_blueprint.add_url_rule('/', view_func=self.audios)
        self.audios_blueprint.add_url_rule('/audios', view_func=self.audios)
        self.audios_blueprint.add_url_rule('/favorites', view_func=self.favorites)

    def audios(self):
        if 'userId' not in session:
                return redirect(url_for('auth.login'))

        user_id = session.get('userId')

        auth = AuthModel()
        user_data = auth.get_user_data(user_id)

        if not user_data:
            return redirect(url_for('auth.login'))


        session['roleId'] = user_data['roleId']
        session['roleName'] = user_data['roleName']

        if session['roleId'] ==1:
            converter = ConverterModel()
            audios = converter.get_all_audios()
        else:
            converter = ConverterModel()
            audios = converter.get_all_by_user(user_id)

        return render_template("Audios/audios.html",  user_data=user_data,roleId=session['roleId'], audios=audios)

    def favorites(self):
            if 'userId' not in session:
                    return redirect(url_for('auth.login'))

            user_id = session.get('userId')



            auth = AuthModel()
            user_data = auth.get_user_data(user_id)



            if not user_data:
                return redirect(url_for('auth.login'))


            session['roleId'] = user_data['roleId']
            session['roleName'] = user_data['roleName']

            if session['roleId'] ==1:
                converter = ConverterModel()
                favorites = converter.get_all_audios_favorites()
            else:
                converter = ConverterModel()
                favorites = converter.get_all_by_user_favorites(user_id)


            return render_template("Audios/favorites.html",favorites = favorites,roleId=session['roleId'],  user_data=user_data)