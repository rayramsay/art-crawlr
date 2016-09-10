import os
import json
from datetime import datetime

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from seed import *

from model import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "my_secret_key"

#raise an error for undefined Jinja variables
app.jinja_env.undefined = StrictUndefined

# Run 'source secrets.sh in terminal'
# Pass Google JS API key to render_template
# gkey = os.environ['GOOGLE_API_KEY']


@app.route('/')
def homepage():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/map.json', methods=['GET'])
def map_json():

    lat = request.args.get('latitude')
    lng = request.args.get('longitude')
    # address = get_address(lat, lng)
    # zipcode = address.split(',')[-2]

    # artworks = db.session.query(Artwork).filter_by(zipcode=zipcode).all()
    # art_list = []
    # for artwork in artworks:
    #     art_list.append({'lat': artwork.lat, 'lng': artwork.lng})
    # print art_list

    art_list = {'waypoints': [{'lat': 37.7975, 'lng': -122.394}, {'lat': 37.7977, 'lng': -122.394}, {'lat': 37.7971, 'lng': -122.398}]}
    art_json = jsonify(art_list)

    print art_json

    return art_json


@app.route('/map', methods=['GET'])
def map_render():
    return render_template("map.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.jinja_env.auto_reload = True
    app.run(host='0.0.0.0')