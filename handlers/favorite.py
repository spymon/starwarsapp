from flask import Blueprint, render_template, session, redirect, url_for

from models.settings import db
from models.user import User

favorite = Blueprint('favorite', __name__)


@favorite.route('/favorite')
def collection():
    if "email" in session:
        email = session['email']
        user = db.query(User).filter_by(email=email).first()

        return render_template("favorite.html", email=user.username)
    else:
        return redirect(url_for('auth.login'))
