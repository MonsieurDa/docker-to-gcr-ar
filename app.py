import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def root():
    return "Hello, World here is my first docker image for gcr"

"""
PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
"""