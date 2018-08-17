from webrpi import app
from flask import request, render_template, session, redirect, url_for
from core import auth

@app.route('/')
def index():
    if 'active' not in session:
        return redirect(url_for('login'))
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'active' in session:
        return redirect(url_for('index'))

    error = None
    if request.method == 'POST':
        if auth.check_login(username=request.form['username'], password=request.form['password']):
            if auth.session_created(username=request.form['username']):
                return redirect(url_for('index'))
            error = 'Invalid session'
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    if auth.session_destroy():
        return redirect(url_for('login'))
    return redirect(url_for('index'))