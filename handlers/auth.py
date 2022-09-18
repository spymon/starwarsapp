from flask import Blueprint, render_template, request, session, redirect, url_for, sessions
import hashlib

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password1')

        # user = User.query.filter_by(email=email).first()
        #
        # if user:
        #     if user.password == hashlib.sha256(password.encode()).hexdigest()
        #         session['username'] = user['username']

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

        # try_user = User.query.filter_by(email=email).first()

        # if try_user:
        #     return "user already exist!"

        if password1 != password2:
            return "passwords does not match!"

        try:
            pass
            # new_user = User(username=username, email=email, password=hashlib.sha256(password1.encode()).hexdigest())
            # db.session.commit()
            # db.session.add(new_user)
        except:
            print("could not save user to the db")

        session['email'] = email

        return redirect(url_for('dashboard.index'))
    else:
        if "email" in session:
            return redirect(url_for('dashboard.index'))

        return render_template('register.html')


@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth.login'))
