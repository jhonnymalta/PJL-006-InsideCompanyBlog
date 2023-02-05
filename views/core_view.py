#core_views.py

from flask import render_template,Blueprint,request
from flask_login import login_required

core = Blueprint('core',__name__)

@core.route("/")
@login_required
def index():
    return render_template('index.html')