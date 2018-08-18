from flask import Flask
from core import db

app = Flask(__name__)

app.secret_key = b'H^a/$-re8SRJ9kZe*(u)u/%{3H~Z\\\O'

db.init_app(app)

import modules.hardware.so
import webrpi.views
