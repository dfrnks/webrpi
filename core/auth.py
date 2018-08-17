from flask import session


def check_login(username, password):
    if(username == "" and password == ""):
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