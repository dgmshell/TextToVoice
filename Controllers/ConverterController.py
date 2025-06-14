from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
<<<<<<< HEAD
class ConverterController:
    def __init__(self):
        self.converter_blueprint = Blueprint('converter', __name__)
        self.converter_blueprint.add_url_rule('/converter', view_func=self.converter)
=======
from Models.ConverterModel import ConverterModel
from gtts import gTTS
import os
import uuid
class ConverterController:
    def __init__(self):
        self.converter_blueprint = Blueprint('converter', __name__)
        self.converter_blueprint.add_url_rule('/', view_func=self.converter)
        self.converter_blueprint.add_url_rule('/converter', view_func=self.converter)
        self.converter_blueprint.add_url_rule('/setConverter', methods=['POST'], view_func=self.setConverter)
        self.converter_blueprint.add_url_rule('/deleteAudioId', methods=['POST'], view_func=self.deleteAudioId)
        self.converter_blueprint.add_url_rule('/addFavorite', methods=['POST'], view_func=self.addFavorite)
>>>>>>> e584ece351510e858fcdb3ce4bcf742b241f31ae

    def converter(self):
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

<<<<<<< HEAD
        print(f"✅ Acceso permitido para: {user_data['userName']} con rol {user_data['roleName']}")

=======
        converter = ConverterModel()
        audios = converter.get_all_audios()
        jsonify(audios)
>>>>>>> e584ece351510e858fcdb3ce4bcf742b241f31ae
        data = {
            "pageName": "dashboard",
            "pageTitle": "Welcome To Dashboard",
            "keywords": "dashboard, panel",
            "description": "Dashboard Admin"
        }

<<<<<<< HEAD
        return render_template("Converter/converter.html", data=data, user_data=user_data)
=======
        return render_template("Converter/converter.html", data=data, user_data=user_data,audios = audios)
    def setConverter(self):
        try:
            userId = session.get('userId')
            data = request.get_json()
            audioId = data.get('audioId', '')
            audioTitle = data.get('audioTitle', 'audio')
            audioText = data.get('audioText', '')
            audioLanguage = data.get('lang', 'es')

            if audioId == "":
                if not audioText.strip():
                    return jsonify({"error": "Texto vacío, no se puede convertir."}), 400

                # Convertir texto a audio con idioma
                tts = gTTS(text=audioText, lang=audioLanguage)

                filename = f"{uuid.uuid4().hex}.mp3"
                folder_path = os.path.join("Assets", "audios")
                os.makedirs(folder_path, exist_ok=True)

                filepath = os.path.join(folder_path, filename)
                tts.save(filepath)

                audioId = f"{filename}"

                return jsonify({
                    "status": "success",
                    "audioId": audioId,
                    "audioTitle": audioTitle
                })
            else:

                converter = ConverterModel()
                response = converter.save(userId,audioId,audioTitle,audioText,audioLanguage)

                return jsonify(response)

#                 return jsonify({
#                     "status": "success",
#                     "message": "Guardar en la db"
#                 })
        except Exception as e:
            print(f"Error en setConverter: {e}")
            return jsonify({"error": "Error interno del servidor."}), 500
    def deleteAudioId(self):
            try:
                data = request.get_json()

                audioId = data.get('audioId2')

                converter = ConverterModel()
                response = converter.delete(audioId)

                return jsonify(response)

            except Exception as e:
                print(f"Error en setProfile: {e}")
                return jsonify({"message": "Error interno del servidor."}), 500
    def addFavorite(self):
            try:
                data = request.get_json()
                userId = data.get('userId')
                audioId = data.get('audioId3')


                converter = ConverterModel()
                response = converter.add(userId,audioId)

                return jsonify(response)

            except Exception as e:
                print(f"Error en setProfile: {e}")
                return jsonify({"message": "Error interno del servidor."}), 500
>>>>>>> e584ece351510e858fcdb3ce4bcf742b241f31ae
