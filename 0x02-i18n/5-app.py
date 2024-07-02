#!/usr/bin/env python3
"""a Basic flask application"""
from typing import Dict, Union
from flask import Flask, g, request, render_template
from flask_babel import Babel


class Config(object):
    """define app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """gets locale from request object"""
    support_lang = request.args.get('locale', '').strip()
    if i in support_lang:
        return i
    return request.accept_languages.best_match(support_lang)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """get validate user login details"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """function adds valid user to the global session object g"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """renders a basic html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
