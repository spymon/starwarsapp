from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from models.settings import db
from models.user import User

user = Blueprint('user', __name__)


@user.route('/profile')
def profile():
    if "email" in session:

        user = db.query(User).filter_by(email=session['email']).first()

        return render_template('user.html', user=user)
    else:
        return redirect(url_for('auth.login'))
