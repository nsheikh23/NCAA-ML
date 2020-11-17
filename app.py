from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from FlaskAPPAML import app
import json
import urllib.request
import os
import rdsconnection as db

app = Flask(__name__, template_folder="templates")
bootstrap = Bootstrap(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:group1final@ncaa-athletics.cr5bt5kg46tf.us-west-1.rds.amazonaws.com/NCAA_Athletics"
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/basketball')
def basketball():
    return render_template(
        'basketball.html',
        basketball_form = basketball_form,
        title = 'Basketball Predictions',
        message = 'Which conference should you go for?'
    )

@app.route('/football')
def football():

    return render_template(
        'football.html',
        football_form = football_form,
        title = "Football Predictions",
        message = "Which conference should you go for?"
    )

with app.test_request_context():
    print(url_for('basketball'))
    print(url_for('football'))

if __name__ == '__main__':
    app.run(debug=True)
