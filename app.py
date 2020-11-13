from flask import Flask, render_template, request, url_for, jsonify
import sqlalchemy
from markupsafe import escape
from bson.json_util import dumps
import aws_controller as db

app = Flask(__name__, template_folder="template")
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:group1final@ncaa-athletics.cr5bt5kg46tf.us-west-1.rds.amazonaws.com/NCAA_Athletics"
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NBA')
def NBA():
    details = db.get_all("NBA")
    print(details)
    # Need to get all players into dictionary form
    # var = {}
    # for detail in details:
        # var = detail
    #     var['pick'] = detail[0]
    #     var['team'] = detail[1]
    #     var['player'] = detail[2]
    #     var['position'] = detail[3]
    # return render_template('index.html', var=var)
    return jsonify(details)

@app.route('/NFL')
def NFL():
    details = db.get_all("NFL")
    print(details)
    # for detail in details:
    #     var = detail
    # return render_template('index.html', var=var)
    return jsonify(details)

# @app.route('/School/<schoolname>')
# def profile(schoolname):
#     return '{}\'s profile'.format(escape(schoolname))

with app.test_request_context():
    print(url_for('NBA'))
    print(url_for('NFL'))
    # print(url_for('profile', username="Duke"))

if __name__ == '__main__':
    app.run(debug=True)
