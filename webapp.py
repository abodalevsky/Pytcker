__author__ = 'abodalevsky'
import os

from flask import Flask

app = Flask(__name__)

COUNTER = 0


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@app.route('/inc')
def inc():
    global COUNTER
    COUNTER += 1
    return '<b>Counter:</b> ' + repr(COUNTER)

@app.route('/dec')
def dec():
    global COUNTER
    COUNTER -= 1
    return '<b>Counter:</b> ' + repr(COUNTER)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

