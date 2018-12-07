from flask import request, Flask
import os
import util
from threading import Thread

app = Flask(__name__)

@app.route('/upload/')
def upload():
    util.upload_image()
    return "success"

@app.route('/finish/')
def finish_upload():
    util.finish_upload()
    return 'finished'

if __name__ == '__main__':

    thread1 = Thread(target=util.detect)
    thread1.start()

    app.run(host='0.0.0.0', port=5000, debug=True)