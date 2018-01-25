"""
Application Main Routes.

This script is simeply for the application to understand the routes of the
application, not nessecarly the order of the in which we use the routes.

We are going to add random text for watchDog

"""

from flask import render_template, request, flash, redirect, url_for
from flaskForms.registrationForm import RegistrationForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    """Index/Landing Page."""
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page."""
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('contact.html',
                               title='Contact',
                               form=form)
    elif request.method == 'POST':
        if not form.validate():
            flash('Enter Required Information')
            return render_template('contact.html',
                                   title='Contact',
                                   form=form)
        else:
            return redirect(url_for('contact'))
