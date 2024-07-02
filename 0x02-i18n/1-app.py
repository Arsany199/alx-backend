#!/usr/bin/env python3
"""model to make a basic babel flask"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """defines the config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """return a template in html file"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
