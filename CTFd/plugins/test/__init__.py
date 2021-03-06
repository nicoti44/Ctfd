import re
import os
from CTFd.plugins import register_plugin_assets_directory
from flask import render_template


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
    scripts = {  # Scripts that are loaded when a template is loaded
        'view': '/plugins/test/static/nicolas.js',
    }

    @staticmethod
    def test():
        return "On est la"


TEST_CLASSES = {"test": CTFdTest}


def load(app):
    #@app.route('/test', methods=['GET'])
    #def view_faq():
     #   return render_template('page.html',
      #                         content="{% extends \"challenge.html\" %}<h1>COUCOU NICOLAS VOILA UN BOUTON</h1><button id=\"fdp\">eho ami</button>")
    register_plugin_assets_directory(app, base_path="/plugins/test/static/")

    @app.route('/start-vm', methods=['POST'])
    def start_vm():
        print('eho server side')
        print('ICI FAIRE DU POWERSHELL')
        # os.system('powershell')
        # os.system('KDKdpz')
        return True

