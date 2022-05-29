#!/usr/bin/python3.8

from tinydb import TinyDB, Query
from flask import Flask, jsonify, request
from tinydb import Query

# creating a Flask app
app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/', methods=['GET'])
def home():
    if(request.method == 'GET'):
        User = Query()
        data = db.search(User.id == 3)

        return jsonify({'data': data})


@app.route('/db/<int:num>', methods=['GET'])
def disp(num):
    User = Query()
    data = db.search(User.id == num)

    return jsonify({'data for this user is': data})


# driver function
if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
:
