import re

from CTFd.plugins import register_plugin_assets_directory
from flask import render_template


def test():
    return True


class BaseTest(object):
    name = None
    templates = {}

    @staticmethod
    def test(self, saved, provided):
        return True


class CTFdTest(BaseTest):
    name = "test"
    templates = {  # Nunjucks templates used for key editing & viewing
        "create": "/plugins/test/static/create.html",
        "update": "/plugins/test/static/edit.html",
        "view": "/plugins/test/page.html",
    }

    @staticmethod
    def test():
        return "On est la"


TEST_CLASSES = {"test": CTFdTest}


def load(app):
    @app.route('/test', methods=['GET'])
    def view_faq():
        return render_template('page.html', content="<h1>COUCOU NICOLAS VOILA UN BOUTON</h1><button>eho ami</button>")



        register_plugin_assets_directory(app, base_path="/plugins/test/static/")
