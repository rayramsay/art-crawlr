import os
import json
from datetime import datetime

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

# from model import *
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "my_secret_key"

#raise an error for undefined Jinja variables
app.jinja_env.undefined = StrictUndefined

# Run 'source secrets.sh in terminal'
# Pass Google JS API key to render_template
gkey = os.environ['GOOGLE_API_KEY']


@app.route('/')
def homepage():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/xplorer')
def xplorer():
    """Page with art xplorer map."""

    return render_template("xplorer.html", gkey=gkey)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0')
