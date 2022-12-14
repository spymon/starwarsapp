import json
import requests
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    if "email" in session:

        res = requests.get('https://akabab.github.io/starwars-api/api/all.json')
        data = json.loads(res.text)

        return render_template("index.html", data=data)
    else:
        return redirect(url_for('auth.login'))

