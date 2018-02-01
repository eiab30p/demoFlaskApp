"""
Configuration File.

The Configuration is simply going to set up your basic needs. For this example
we are going to enable cross-site request forgery or CSRF. This helps with
prevention of unauthorized commands to be transmitted from the app.

The SECRET_KEY is in fact redicoulse for a reason but it is only needed when
CSRF is enabled, and is used to create a cryptographic token that is used to
validate a form.

"""
from os.path import join, dirname
from dotenv import load_dotenv
import os

# Reding from a .env file for environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY')

# email server
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
