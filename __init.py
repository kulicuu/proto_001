

import model


import sys
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json


from requests.exceptions import HTTPError

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/mymodel/add', methods=['POST'])
def add():
    data = request.get_json(force=True)
    print(str(data) + 'data', file=sys.stderr)
    try:
        x = int(data['x'])
        y = int(data['y'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(answer = x + y)


@app.route('/mymodel/subtract', methods=['POST'])
def subtract():
    data = request.get_json(force=True)
    print(str(data) + 'data', file=sys.stderr)
    try:
        x = int(data['x'])
        y = int(data['y'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(answer = x - y)


if __name__ == '__main__':
    app.run()
