# System import
from flask import Flask, render_template, redirect, url_for, request

# core import
from core.AppCore import AppCore
from database.DatabaseController import DatabaseController

# keys import 
from core.constants.KeysApi import KeysApi

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    """Renders a sample page."""
    AppCore.RequestFreeCompanyData(KeysApi.LODESTONE_ID_CL)
    return render_template('index.html', fc_name='ETHER')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        print(request.form)
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
