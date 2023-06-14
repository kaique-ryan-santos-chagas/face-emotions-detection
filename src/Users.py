import sqlite3 as database 

from src.database.DatabaseMethods import DatabaseMethods

class User:

    def __init__(self, user_data):

        self.user_data = user_data['user_data']
        self.connection = database.connect('face_emotion_detection.db')
        

    def register_user(self):

        query = DatabaseMethods(self.connection)
        result = query.register_user(self.user_data)

        return result
