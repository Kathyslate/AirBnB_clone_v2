#!/usr/bin/python3
"""advanced task"""

from flask import Flask, render_template
from models import storage
from os import getenv
from models import storage

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a HTML page like 8-index.html"""
    storage.close()
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template("100-hbnb.html", states=states, cities=cities, amenities=amenities, places=places)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
