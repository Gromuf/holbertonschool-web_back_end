#!/usr/bin/env python3
""" App module """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route("/", methods=["GET"])
def home():
    """ Returns a welcome message """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
