#!/usr/bin/env python3
""" App module """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """ Config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """ Determine the best match for supported languages """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    elif g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    headers_locale = request.headers.get('Locale')
    if headers_locale in app.config['LANGUAGES']:
        return headers_locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get user from request """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@babel.timezoneselector
def get_timezone():
    """ Get timezone from user """
    if request.args.get('timezone'):
        try:
            pytz.timezone(request.args.get('timezone'))
            return request.args.get('timezone')
        except pytz.UnknownTimeZoneError:
            pass
    if g.get('user'):
        if g.user.get('timezone'):
            try:
                pytz.timezone(g.user.get('timezone'))
                return g.user.get('timezone')
            except pytz.UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """ Set user before each request """
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/", methods=["GET"])
def home():
    """ Returns a welcome message """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
