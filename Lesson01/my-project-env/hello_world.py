# This is the first program on flask

import os
from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>/')
def hello_world(name):
    return 'Hello, {}!'.format(name)


@app.route('/goodbye/<times>/<name>/')
def goodbye_world(times, name):
    return ('|, {}!'.format(name)) * int(times)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)


