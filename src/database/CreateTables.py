import sqlite3 as sqlite 

database = sqlite.connect('face_emotion_detection.db')

database.execute('CREATE TABLE IF NOT EXISTS pending_analyses (id INTEGER PRIMARY KEY AUTOINCREMENT, file_name VARCHAR(30), date_register DATE, age_group VARCHAR(20), audiovisual_production VARCHAR(50), user_id INTEGER)')

database.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30), user_email VARCHAR(30))')