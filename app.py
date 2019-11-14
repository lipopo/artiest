import sys
import os

from flask import Flask, jsonify, render_template
import jinja2


# import local package
sys.path.insert(0, os.path.dirname(__file__))
from setting import setting


pwd_folder = os.path.dirname(__file__)
template_folder=os.path.join(pwd_folder, 'static')
app = Flask(
    __name__,
    static_folder=os.path.join(pwd_folder, 'static'),
    static_url_path='/'
)
app.jinja_loader = jinja2.FileSystemLoader(template_folder, encoding='utf-8')
__version__ = open("version.txt", "r").read()


@app.route('/')
def index():
    return render_template('html/coming_soon.html')


@app.route('/test')
def test():
    return render_template('html/index.html', **setting.website_setting)


@app.route('/version')
def version():
    return jsonify(
        {
            'version': __version__
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8888)), debug=True)
