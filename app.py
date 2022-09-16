import json
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from handlers.auth import auth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localhost.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = b'secret indeed'
app.register_blueprint(auth)


@app.route('/')
def index():
    res = requests.get('https://akabab.github.io/starwars-api/api/all.json')
    data = json.loads(res.text)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
