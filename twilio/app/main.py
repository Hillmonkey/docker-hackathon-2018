#!/usr/bin/python3
"""Simple Flask web application"""

import os
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
    call_from = os.environ['TWILIO_FROM']
    call_to_default = os.environ['TWILIO_TO']
    num_texts = sms.hammer_sms(request.json['msg'], call_from, call_to_default)
    return jsonify({'texts': str(len(texts))}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
