
"""
Initializing Application.

The script above simply creates the application object (of class Flask).
and then imports the views module, which we haven't written yet. Do not
confuse app the variable (which gets assigned the Flask instance) with
app the package (from which we import the views module).

Other Stuff Gose Here
"""

from flask import Flask
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_session import Session
from flask_socketio import SocketIO, emit
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object('config')

csrf = CSRFProtect(app)

app.config['SESSION_TYPE'] = 'filesystem'
login = LoginManager(app)
Session(app)
socketio = SocketIO(app, manage_session=False)

mail = Mail(app)

from app import views
