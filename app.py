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
    details = db.get_all()
    # print(details)
    for detail in details:
        var = detail
    return render_template("index.html")

@app.route('/basketball')
def basketball():
    bball_key = os.environ.get('API_KEY', "3ykY3j9WZDYvS0Dvf5VoJ1kA0yVT5HVzT+foY4SzKvD6LJhHoysBjlEQWaOniNQCGqsjKrytONq1kdxEWo3Scg==")
    bball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true")
    
    B_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ bball_key)}

    return render_template(
        'basketball.html',
        basketball_form = basketball_form,
        title = 'Basketball Predictions',
        message = 'Which conference should you go for?'
    )

@app.route('/football')
def football():
    fball_key = os.environ.get('API_KEY', "3ykY3j9WZDYvS0Dvf5VoJ1kA0yVT5HVzT+foY4SzKvD6LJhHoysBjlEQWaOniNQCGqsjKrytONq1kdxEWo3Scg==")
    fball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true")

    F_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ fball_key)}

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
