#! /usr/bin/env python

import redis
import json
from flask import Flask
from math import factorial

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World !\n'

@app.route('/factorial')
def get_key_factorial():
    """
    Fetch a key and compute the factorial of the returned value

    Some Test keys ['drepr', 'djejv', 'dzpjb']
    """
    db = redis.Redis(host='redis', port=6379, decode_responses=True)
    for key in db.scan_iter():
        num = int(db.get(key))
        res = factorial(num)
        break
    return json.dumps(res), 200

if __name__ == '__main__':
    app.run(port=5000, debug=False, host='0.0.0.0')
