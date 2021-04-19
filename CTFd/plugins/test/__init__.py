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


class CTFdTest(BaseFlag):
    name = "test"
    templates = {  # Nunjucks templates used for key editing & viewing
        "create": "/plugins/test/static/create.html",
        "update": "/plugins/test/static/edit.html",
        "view": "/plugins/test/page.html",
    }

    @staticmethod
    def test():
        return "On est la"


FLAG_CLASSES = {"static": CTFdStaticFlag, "regex": CTFdRegexFlag}



def load(app):
 @app.route('/test', methods=['GET'])
    def view_faq():
        return render_template('static/page.html', content="<h1>COUCOU NICOLAS VOILA UN BOUTON</h1><button onclick="alert('jui un haxer')">eho ami</button>")



    register_plugin_assets_directory(app, base_path="/plugins/flags/static/")

