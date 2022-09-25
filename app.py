from flask import Flask
from handlers.auth import auth
from handlers.dashboard import dashboard
from handlers.favorite import favorite
from handlers.user import user


app = Flask(__name__)

app.secret_key = b'secret indeed'
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(favorite)
app.register_blueprint(user)


if __name__ == "__main__":
    app.run(debug=True)
