from flask import Flask, render_template, request, url_for, jsonify
from markupsafe import escape
from bson.json_util import dumps
import aws_controller as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NBA')
def NBA():
    details = db.get_all("NBA")
    print(details)
    for detail in details:
        var = detail
    return render_template('index.html', var=var)
    # return jsonify(aws_controller.get_all("NBA"))

@app.route('/NFL')
def NFL():
    details = db.get_all("NFL")
    print(details)
    for detail in details:
        var = detail
    return render_template('index.html', var=var)
    # return jsonify(aws_controller.get_all("NFL"))

# @app.route('/School/<schoolname>')
# def profile(schoolname):
#     return '{}\'s profile'.format(escape(schoolname))

with app.test_request_context():
    print(url_for('NBA'))
    print(url_for('NFL'))
    print(url_for('profile', username="Duke"))

if __name__ == '__main__':
    app.run(debug=True)
