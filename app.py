# System import
from flask import Flask, render_template

# core import
from core.AppCore import AppCore

# keys import 
from core.constants.KeysApi import KeysApi

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    """Renders a sample page."""
    AppCore.RequestAchievementsDetail("1")
    return render_template('index.html', fc_name='ETHER')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
