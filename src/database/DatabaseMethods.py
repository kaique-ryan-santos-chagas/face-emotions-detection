import json

from datetime import date

class DatabaseMethods:

    def __init__(self, connection):

        self.database = connection


    def register_pending_analyse(self, video_data):

        filename = video_data['filename']
        user_email = video_data['user_email']
        age_group = video_data['age_group']
        gender = video_data['gender']
        date_today = date.today()

        self.database.execute('INSERT INTO pending_analyses (file_name, user_email, date_register) VALUES ("'+ filename +'", "'+ user_email +'", "'+ str(date_today) +', '+ age_group +', '+ gender +' ") ')
        
        return 'Analyse stored successfull.'

    
    def delete_pending_analyse(self, pending_analyse_id):

        self.database.execute('DELETE FROM pending_analyses WHERE id = ' + str(pending_analyse_id))
        self.database.commit()
        
        return 'Analyse deleted successfull.'

    
    def get_pending_analyse(self):

        pending_analyse = self.database.execute('SELECT * FROM pending_analyses LIMIT 1')
        analyse = pending_analyse.fetchall()

        return analyse
    
    def get_user_data(self, user_email):

        user_data = self.database.execute("SELECT * FROM users WHERE user_email = '" + user_email + "'")

        return user_data.fetchall()
    

    def register_user(self, user_data_json):

        user_data = json.loads(user_data_json)

        username = user_data.username
        useremail = user_data.useremail

        self.database.execute('INSERT INTO users (name, user_email) VALUES ("'+ username +'", "'+ useremail +'")')

        return 'User registered successfully.'
    
