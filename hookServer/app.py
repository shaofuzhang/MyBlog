import os
import logging
from flask import Flask, Response, abort
from logging.handlers import TimedRotatingFileHandler
import json


class NonASCIIJSONEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        super(NonASCIIJSONEncoder, self).__init__(**kwargs)

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, bytes):
            return o.decode('utf-8')

        return json.JSONEncoder.default(self, o)


def create_app():
    app = Flask(__name__)
    logfile = os.path.join(app.root_path, 'log/log.log')
    if not os.path.exists(os.path.dirname(logfile)):
        os.mkdir(os.path.dirname(logfile))
    file_handler = TimedRotatingFileHandler(logfile, 'D', 1, 15)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
    # app.logger.setLevel(app.config.get('LOGGING_LEVEL'))
    file_handler.setLevel(app.config.get('LOGGING_LEVEl', logging.DEBUG))
    app.logger.addHandler(file_handler)

    app.json_encoder = NonASCIIJSONEncoder
    return app


app = create_app()
sh_path = os.path.join(app.root_path[:app.root_path.rfind('/')], "publish.sh")


@app.route('/', methods=['POST'])
@app.route('/deploy')
def index():
    os.system(sh_path)
    return "ok"


@app.route("/image/<image_name>")
def get_image(image_name):
    img_path = app.root_path + '/static/' + image_name
    mdict = {
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif'
    }
    mime = mdict[image_name[image_name.rfind(".") + 1:]]
    if not os.path.exists(img_path):
        # Res 是我自己定义的返回类，raw方法将数据组成字典返回
        abort(404)
    with open(img_path, 'rb') as f:
        image = f.read()
    return Response(image, mimetype=mime)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6767, debug=False, threaded=True)
