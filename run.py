#!flask/bin/python
"""
Running Application.

imports the app variable from our app package and invokes its run method
to start the serve

"""
from app import app
app.run(host='0.0.0.0', port=5000, debug=True)
