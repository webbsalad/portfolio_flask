from app import app


if __name__ == '__main__':
    app.run(debug=False)


#pybabel extract -F babel.cfg -o messages.pot .
#pybabel init -i messages.pot -d translations -l en
# pybabel compile -d translations   