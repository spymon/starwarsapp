import hashlib

from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from models.settings import db
from models.user import User

user = Blueprint('user', __name__)


@user.route('/profile')
def profile():
    if "email" in session:

        logged_user = db.query(User).filter_by(email=session['email']).first()

        return render_template('user.html', user=logged_user)
    else:
        return redirect(url_for('auth.login'))


@user.route('/change-password', methods=["GET", "POST"])
def change_password():
    if 'email' in session:
        logged_user = db.query(User).filter_by(email=session['email']).first()
        if request.method == "POST":
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            if password1 != password2:
                flash("Passwords does not match!", "danger")
                return redirect(url_for('user.change_password'))

            logged_user.password = hashlib.sha256(password1.encode()).hexdigest()
            db.add(logged_user)
            db.commit()

            flash("Password changed successfully", "success")
            return redirect(url_for('user.profile'))

        if request.method == 'GET':
            return render_template('change_password.html')
    else:
        return redirect(url_for('auth.login'))


@user.route('/change-username', methods=["GET", "POST"])
def change_username():
    if 'email' in session:
        logged_user = db.query(User).filter_by(email=session['email']).first()
        if request.method == "POST":
            username = request.form.get('username')

            logged_user.username = username
            db.add(logged_user)
            db.commit()

            flash("Username changed successfully", "success")
            return redirect(url_for('user.profile'))

        if request.method == 'GET':
            return render_template('change_username.html')
    else:
        redirect(url_for('auth.login'))


@user.route('/delete-user', methods=["POST"])
def delete_user():
    if 'email' in session:
        logged_user = db.query(User).filter_by(email=session['email']).first()

        if request.method == 'POST':
            delete_password = request.form.get('password')
            if logged_user.password == hashlib.sha256(delete_password.encode()).hexdigest():
                db.delete(logged_user)
                db.commit()
                session.pop('email', None)

                flash("User deleted successfully", "success")
                return redirect(url_for('auth.login'))
            else:
                flash("Incorrect password", "danger")
                return redirect(url_for('user.profile'))

    else:
        return redirect(url_for('auth.login'))
