import os
import time
from async_api_call import async_api_call
from sync_api_call import sync_api_calls
import asyncio
from flask import Flask, render_template, send_from_directory
from flask import jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
async_route = '/async'
sync_route = '/sync'


@app.route('/')
def home():
    return render_template('base.html')


def read_data():
    with open('postal_code_data.txt') as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


@app.route(async_route)
def async_api():
    postal_code = read_data()
    start = time.perf_counter()
    data = asyncio.run(async_api_call(postal_code))
    end = time.perf_counter()
    processing_time = end - start
    contents = {
        'time': processing_time,
        'results': data
    }
    return jsonify(contents)


@app.route(sync_route)
def sync_api():
    postal_code = read_data()
    start = time.perf_counter()
    data = sync_api_calls(postal_code)
    end = time.perf_counter()
    processing_time = end - start
    contents = {
        'time': processing_time,
        'results': data
    }
    return jsonify(contents)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favico.png', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()
