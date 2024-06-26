#!/usr/bin/env python3
"""a simple Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """return a simple string"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
