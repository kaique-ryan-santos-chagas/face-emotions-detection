import sqlite3 as sqlite 

database = sqlite.connect('face_emotion_detection.db')

database.execute('CREATE TABLE IF NOT EXISTS pending_analyses (id INTEGER PRIMARY KEY AUTOINCREMENT, file_name VARCHAR(30), user_email VARCHAR(30), date_register DATE)')
