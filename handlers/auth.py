from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import hashlib

from models.settings import db
from models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.query(User).filter_by(email=email).first()
        if user:
            if user.password == hashlib.sha256(password.encode()).hexdigest():
                session['email'] = user.email
                session['username'] = user.username
            else:
                flash("Incorrect credentials", "danger")
                return redirect(url_for('auth.login'))
        else:
            flash("Incorrect credentials", "danger")
            return redirect(url_for('auth.login'))

        flash("Logged in successfully", "success")
        return redirect(url_for('dashboard.index'))
    else:
        if "email" in session:
            return redirect(url_for('dashboard.index'))

        return render_template('login.html')


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        try_user = db.query(User).filter_by(email=email).first()

        if password1 != password2:
            flash("Passwords does not match!", "danger")
            return redirect(url_for('auth.register'))

        if try_user:
            flash("User already exist!", "danger")
            return redirect(url_for('auth.register'))

        new_user = User(username=username, email=email, password=hashlib.sha256(password1.encode()).hexdigest())
        db.add(new_user)
        db.commit()

        session['email'] = new_user.email
        session['username'] = new_user.username

        flash("Logged in successfully", "success")
        return redirect(url_for('dashboard.index'))
    else:
        if "email" in session:
            return redirect(url_for('dashboard.index'))

        return render_template('register.html')


@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth.login'))
