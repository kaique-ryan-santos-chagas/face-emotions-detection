import sqlite3 as sqlite 

database = sqlite.connect('face_emotion_detection.db')

database.execute('CREATE TABLE IF NOT EXISTS pending_analyses (id INTEGER PRIMARY KEY AUTOINCREMENT, file_name VARCHAR(30), user_email VARCHAR(30), date_register DATE)')

database.execute('INSERT INTO pending_analyses (file_name, user_email, date_register) VALUES ("test", "test", 2023-03-17)')