import os
from dotenv import load_dotenv

load_dotenv()

class Helpers:
    @staticmethod
    def get_env_variable(var_name, default=None):
        return os.getenv(var_name, default)

    @staticmethod
    def url_files():
        return Helpers.get_env_variable("URL_FILES", "http://127.0.0.1:5000/Assets/")

    @staticmethod
    def url_base():
        return Helpers.get_env_variable("URL_BASE", "http://127.0.0.1:5000/")
