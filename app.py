import time, asyncio, concurrent

import werkzeug.exceptions
from flask import Flask, request, render_template, jsonify
from flask_celery import make_celery
from celery import Celery


app = Flask(__name__)
app.config['SECRET_KEY'] = '121523b3etetbw4tw3v3w3vw4v'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['TOKEN'] = "TOKEN"
celery = make_celery(app)


@celery.task
def create_file(context):
    time.sleep(5)
    print("ok")

        # f.write(context)


@celery.task
def validate_content(datas):
    # headers = request.headers
    _valid_datas = ['title', 'content']
    _warnings = []
    _accepted = {}
    for data in _valid_datas:
        if not datas.get(data, False):
            _warnings.append(data)

    if not _warnings:
        print("salom")
        with open(f"celery_files/{datas['title']}.txt", 'w') as f:
            f.write(datas['content'])

        return jsonify({"data": "created"})
    return jsonify({"data": {"please complete all fields": _warnings}})


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        auth = request.headers.get('X-Api-Key')
        if not auth == app.config['TOKEN']:
            return jsonify({"message": "ERROR: Unauthorized"}), 401

        validate_content.delay(request.json)
        return "salom"
    else:
        return jsonify(method=request.method)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return jsonify({
        "data": "bad request"
    }), 404


app.register_error_handler(404, handle_bad_request)
# app.register_error_handler(500, handle_bad_request)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
