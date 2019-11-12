import sys
import os

from flask import Flask, jsonify


# import local package
sys.path.insert(0, os.path.dirname(__file__))
from setting import setting


app = Flask(__name__)
__version__ = '0.0.1'


@app.route('/')
def index():
    return ''


@app.route('/version')
def version():
    return jsonify(
        {
            'version': __version__
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8888)), debug=True)
