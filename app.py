from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__, static_url_path='/static', static_folder='static')
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'


def get_locale():
    return request.args.get('lang') or \
           request.accept_languages.best_match(['en', 'ru'])

babel.init_app(app, locale_selector=get_locale)

    
@app.route('/')
def index():
    return render_template("index.html", get_locale=get_locale)

@app.route('/about')
def about():
    return render_template("about.html", get_locale=get_locale)

@app.route('/prog')
def prog():
    return render_template("prog.html", get_locale=get_locale)

@app.route('/db')
def db():
    return render_template("db.html", get_locale=get_locale)

@app.route('/cw')
def cw():
    return render_template("cw.html", get_locale=get_locale)

@app.route('/swt')
def swt():
    return render_template("swt.html", get_locale=get_locale)
