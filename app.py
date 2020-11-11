from flask import Flask, render_template, request, jsonify
from bson.json_util import dumps
import aws_controller as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NBA', methods=['GET'])
def NBA():
    if request.method == "GET":
        details = db.get_all("NBA")
        print(details)
        for detail in details:
            var = detail
    return render_template('index.html', var=var)
    # return jsonify(aws_controller.get_all("NBA"))

@app.route('/NFL', methods=['GET'])
def NFL():
    if request.method == "GET":
        details = db.get_all("NFL")
        print(details)
        for detail in details:
            var = detail
    return render_template('index.html', var=var)
    # return jsonify(aws_controller.get_all("NFL"))

if __name__ == '__main__':
    app.run(debug=True)
