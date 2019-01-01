from webrpi import app
from flask import render_template, session, redirect, url_for
import platform
import time


@app.route("/dispositivos/<id>")
def active(id):
    if 'active' not in session:
        return redirect(url_for('login'))

    time.sleep(2)  # DO Something

    return redirect(url_for('index'))
