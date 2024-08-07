#!/usr/bin/env python3
"""model Basic flask application"""
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """defines app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """function that display validate user login details"""
    return users.get(int(id), {})


@babel.localeselector
def get_locale():
    """function gets locale from request object"""
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.before_request
def before_request():
    """function adds valid user to the global session object g"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/')
def index():
    """function renders a basic html template"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
