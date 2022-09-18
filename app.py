from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from handlers.auth import auth
from handlers.dashboard import dashboard
from handlers.favorite import favorite


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localhost.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = b'secret indeed'
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(favorite)


if __name__ == "__main__":
    app.run(debug=True)
