from webrpi import app
from flask import render_template, session, redirect, url_for
import platform


@app.route("/hardware/status")
def getStatus():
    if 'active' not in session:
        return redirect(url_for('login'))

    data = dict(
        node=platform.node(),
        uname=platform.uname(),
        system=platform.system(),
        release=platform.release(),
        version=platform.version(),
        machine=platform.machine(),
        processor=platform.processor(),
        architecture=platform.architecture(),
        platform=platform.linux_distribution(),
    )

    return render_template('hardware/so/status.html', data=data)
