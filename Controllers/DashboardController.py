from flask import Blueprint, render_template, session, request,jsonify, redirect, url_for
from Models.AuthModel import AuthModel
class DashboardController:
    def __init__(self):
        self.dashboard_blueprint = Blueprint('dashboard', __name__)
        self.dashboard_blueprint.add_url_rule('/dashboard', view_func=self.dashboard)

    def dashboard(self):
        data = {
                "pageName": "dashboard",
                "pageTitle": "Welcome To Dashboard",
                "keywords": "dashboard, panel",
                "description": "Dashboard "
                }
        return render_template('/Dashboard/dashboard.html', data=data)
