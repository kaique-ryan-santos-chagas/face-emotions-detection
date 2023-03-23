from flask import Flask, jsonify
from src.Job import Job 

import threading
import sqlite3 as database

# start job listen in second thread.

def run_scheduler():

    connection = database.connect('face_emotion_detection.db')

    job = Job(connection)

    while True:
        job.start_detection()

job_thread = threading.Thread(target=run_scheduler)
job_thread.start()


# start server in main thread. 

app = Flask(__name__)

@app.route('/')

def welcome():
    return 'Welcome to Face Emotion Detection to audiovisual productions!'


@app.route('/send/video')

def send_video():

    return jsonify('name: Kaique Ryan')


if __name__ == '__main__':
    app.run()