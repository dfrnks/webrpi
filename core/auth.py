from flask import session
from core.db import db


def check_login(username, password):
    count = db().execute('SELECT count(*) as qtd FROM user').fetchone()

    if count["qtd"] == 0:
        db().execute('INSERT INTO user (username, password) VALUES (?,?)', ('admin','admin'))
        db().commit()

    user = db().execute('SELECT password FROM user where username = ?', (username, )).fetchone()

    if not user:
        return False

    if(password == user["password"]):
        return True
    else:
        return True

def session_created(username):
    session['active'] = True
    session['username'] = username

    return True

def session_destroy():
    session.pop('active', None)

    return True