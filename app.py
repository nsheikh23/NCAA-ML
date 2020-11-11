from flask import Flask, render_template, redirect, jsonify
from bson.json_util import dumps
import aws_controller

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NBA')
def NBA():
    return jsonify(aws_controller.get_all("NBA"))

@app.route('/NFL')
def NFL():
    return jsonify(aws_controller.get_all("NFL"))

if __name__ == '__main__':
    app.run(debug=True)
