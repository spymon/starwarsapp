from flask import Blueprint, render_template, session, redirect, url_for

favorite = Blueprint('favorite', __name__)


@favorite.route('/favorite')
def collection():
    if "email" in session:
        email = session['email']
        # user = User.query.filter_By(email=email).first()

        return render_template("favorite.html", email=email)
    else:
        return redirect(url_for('auth.login'))
