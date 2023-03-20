from flask import Flask, jsonify
from src.Job import Job 

import threading

app = Flask(__name__)
job = Job()

def run_scheduler():
    while True:
        job.start_detection()

job_thread = threading.Thread(target=run_scheduler)
job_thread.start()

@app.route('/')

def welcome():
    return 'Welcome to Face Emotion Detection to audiovisual productions!'


@app.route('/send/video')

def send_video():

    return jsonify('name: Kaique Ryan')


if __name__ == '__main__':
    app.run()