from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
class HomeController:
    def __init__(self):
        self.home_blueprint = Blueprint('/home', __name__)

        self.home_blueprint.add_url_rule('/', view_func=self.home)
        self.home_blueprint.add_url_rule('/home', view_func=self.home)

    def home(self):
        data = {
                "pageName": "home",
                "pageTitle": "Welcome To Home",
                "keywords": "home, home",
                "description": "Home "
                }
        return render_template('home.html', data=data)
