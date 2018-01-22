"""
Initializing Application.

The script above simply creates the application object (of class Flask).
and then imports the views module, which we haven't written yet. Do not
confuse app the variable (which gets assigned the Flask instance) with
app the package (from which we import the views module).

Other Stuff Gose Here
"""

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    """Root For All Web Pages."""
    print("testing")
    return render_template("based.html")
