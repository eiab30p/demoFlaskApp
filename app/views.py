"""
Application Main Routes.

This script is simeply for the application to understand the routes of the
application, not nessecarly the order of the in which we use the routes.

We are going to add random text for watchDog

"""

from flask import render_template, request, flash, redirect, url_for
from flaskForms.registrationForm import RegistrationForm
from app import app
from util.emailFunction import configEmailTemp
from flask_wtf.csrf import CSRFError
import os


@app.route('/')
@app.route('/index')
def index():
    """Index/Landing Page."""
    try:
        linkedIn = os.environ.get('LINKEDIN')
        github = os.environ.get('GITHUB')
    except Exception as e:
        app.logger.error('Environment Did Not Set or Did Not Establish: %s',
                         (e))

    return render_template('index.html',
                           linkedInURL=linkedIn,
                           gitHubURL=github)


@app.route('/about', methods=['POST', 'GET'])
def about():
    """About Page."""
    if request.method == 'GET':
        return render_template('about.html',
                               title='About')


@app.route('/knowledge', methods=['POST', 'GET'])
def knowledge():
    """Knowledge Section."""
    if request.method == 'GET':
        return render_template('knowledge.html',
                               title='knowledge')


@app.route('/travel')
def travel():
    """Travel Page Possible Reroute."""
    if request.method == 'GET':
        return render_template('travel.html',
                               title='Travel')


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
            try:
                configEmailTemp(form.data)
            except Exception as e:
                app.logger.error('Issue Creating Email: %s', (e))
                flash(e)
                return render_template('contact.html',
                                       title='Contact',
                                       form=form)

            return redirect(url_for('contact'))


# Admin Reroute MicroService?

@app.route('/signin', methods=['POST', 'GET'])
@app.route('/admin', methods=['POST', 'GET'])
def admin():
    """Admin Page possible Reroute."""
    return render_template('index.html',
                           title='admin')

# Blog Reroute MicroService?


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    """Blog Page possible Reroute."""
    if request.method == 'GET':
        return render_template('index.html',
                               title='blog')


@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(410)
@app.errorhandler(500)
def page_not_found(e):
    """Error Page."""
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template("404.html",
                           title=e)
