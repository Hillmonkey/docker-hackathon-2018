#!/usr/bin/python3
"""Simple Flask web application"""

from flask import Flask, jsonify
import sms_tasks as sms
from flask import request
from flask import make_response

app = Flask('__name__')
app.url_map.strict_slashes = False


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/larry', methods=['POST'])
def text_larry():
    '''accepts json:{'msg':<str>}
    breaks string into words and sends each word as a separate text msg
    '''
    if not request.json or 'msg' not in request.json:
        abort(400)
    num_texts = sms.hammer_sms(request.json['msg'], '4154818386')
    return jsonify({'texts': str(len(texts))}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
