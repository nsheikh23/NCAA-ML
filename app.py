from flask import Flask, render_template, redirect, jsonify
from bson.json_util import dumps
import aws_controller

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gatherData')
def get_all():
    return jsonify(aws_controller.get_all())

# @app.route('/do_items/')
# def do_items():
#     response=aws_controller.create_table()
#     return response

# @app.route('/do_items')
# def do_items(table):
#     response=aws_controller.create_table(table)
#     return response

# @app.route('/get-items/')
# def get_items():
#     return jsonify(aws_controller.get_item())

if __name__ == '__main__':
    app.run(debug=True)
