from flask import Flask, render_template, request
from flask_babel import Babel, _
import requests

app = Flask(__name__, static_url_path='/static', static_folder='static')
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

def get_locale():
    return request.args.get('lang') or \
           request.accept_languages.best_match(['en', 'ru'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", get_locale=get_locale)
    elif request.method == 'POST':
        return 'это пост запрос)'

@app.route('/about')
def about():
    return render_template("about.html", get_locale=get_locale)

@app.route('/prog')
def prog():
    response = requests.get('https://portfolio-rest-api-kohl.vercel.app/prog')
    labs = response.json() if response.status_code == 200 else []
    return render_template("prog.html", labs=labs, get_locale=get_locale)

@app.route('/db')
def db():
    response = requests.get('https://portfolio-rest-api-kohl.vercel.app/db')
    labs = response.json() if response.status_code == 200 else []
    return render_template("db.html", labs=labs, get_locale=get_locale)

@app.route('/cw')
def cw():
    response = requests.get('https://portfolio-rest-api-kohl.vercel.app/cw')
    labs = response.json() if response.status_code == 200 else []
    return render_template("cw.html", labs=labs, get_locale=get_locale)

@app.route('/swt')
def swt():
    response = requests.get('https://portfolio-rest-api-kohl.vercel.app/swt')
    labs = response.json() if response.status_code == 200 else []
    return render_template("swt.html", labs=labs, get_locale=get_locale)

if __name__ == '__main__':
    app.run(debug=True)
