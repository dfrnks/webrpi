from flask import Flask

app = Flask(__name__)

app.secret_key = b'H^a/$-re8SRJ9kZe*(u)u/%{3H~Z\\\O'

import modules.hardware.so
import webrpi.views
