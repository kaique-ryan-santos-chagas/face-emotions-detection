from flask import Flask, request, jsonify
from src.Job import Job 
from src.EmotionDetection import EmotionDetection

import threading
import sqlite3 as database
import os

# start job listen in second thread.

connection = database.connect('face_emotion_detection.db', check_same_thread=False)
emotionDetection = EmotionDetection(connection)

job = Job(connection)

job_thread = threading.Thread(target=job.run_scheduler)
job_thread.start()

# start server in main thread. 

app = Flask(__name__)

@app.route('/')

def welcome():

    return 'Welcome to Face Emotion Detection to audiovisual productions!'


@app.route('/send/video', methods=['POST'])
    
def store_video():

    analyse_data = request.form['json_data']
    video_file_zip = request.files['file']
    zip_folder_path = os.path.join(os.getcwd(), 'zipfiles')
    video_path = os.path.join(zip_folder_path, video_file_zip.filename)

    filename, extension = os.path.splitext(video_file_zip.filename)

    if not extension == '.zip':

        return jsonify({'message': 'Error: this file is in incorrect format.'})

    video_file_zip.save(video_path)
    emotionDetection.store_pending_analyse(analyse_data)

    return jsonify({'message': 'Video stored succesfull.'})


if __name__ == '__main__':
    app.run()