from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/prog')
def prog():
    return render_template("prog.html")

@app.route('/db')
def db():
    return render_template("db.html")

@app.route('/cw')
def cw():
    return render_template("cw.html")

@app.route('/swt')
def swt():
    return render_template("swt.html")

