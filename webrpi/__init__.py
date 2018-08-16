from flask import Flask

app = Flask(__name__)

import modules.hardware.so
import webrpi.views
