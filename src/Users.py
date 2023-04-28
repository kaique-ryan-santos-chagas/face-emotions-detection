import sqlite3 as database 
import json

from src.database.DatabaseMethods import DatabaseMethods

class User:

    def __init__(self, user_data):

        self.username = ''
        self.useremail = ''
        self.connection = database.connect('face_emotion_detection.db')
        

    def register_user(self):

        query = DatabaseMethods(self.connection)
        user_data = json.dumps({ 'username': self.username, 'useremail': self.useremail })
        result = query.register_user(user_data)

        return result
