#!/usr/bin/env python3
""" App module """
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """ Returns a welcome message """
    return jsonify({"message": "Bienvenue"})