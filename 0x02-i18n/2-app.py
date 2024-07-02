#!/usr/bin/env python3
"""model to make a basic babel flask"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """defines the config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """function to determine the best match with the supported lang."""
    return request.accept_language.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """return a template in html file"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
