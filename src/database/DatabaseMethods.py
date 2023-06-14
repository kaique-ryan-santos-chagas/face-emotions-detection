from datetime import date

class DatabaseMethods:

    def __init__(self, connection):

        self.database = connection


    def register_pending_analyse(self, video_data):

        filename = video_data['filename']
        age_group = video_data['age_group']
        audiovisual_production = video_data['audiovisual_production']
        user_id = video_data['user_id']
        date_today = date.today()

        self.database.execute('INSERT INTO pending_analyses (file_name, date_register, age_group, audiovisual_production, user_id) VALUES ("'+ filename +'", "'+ str(date_today) +'", "'+ age_group +'", "'+ audiovisual_production +'", "'+ str(user_id) +'") ')
        self.database.commit()

        return 'Analyse stored successfully.'

    
    def delete_pending_analyse(self, pending_analyse_id):

        self.database.execute('DELETE FROM pending_analyses WHERE id = ' + str(pending_analyse_id))
        self.database.commit()
        
        return 'Analyse deleted successfully.'

    
    def get_pending_analyse(self):

        pending_analyse = self.database.execute('SELECT * FROM pending_analyses LIMIT 1')
        analyse = pending_analyse.fetchall()

        return analyse
    
    def get_user_data(self, user_email):

        user_data = self.database.execute("SELECT * FROM users WHERE user_email = '" + user_email + "'")

        return user_data.fetchall()
    
    def get_user_data_by_id(self, user_id):

        user_data = self.database.execute("SELECT * FROM users WHERE id = '" + str(user_id) + "'")

        return user_data.fetchall()
    

    def register_user(self, user_data):

        username = user_data['username']
        useremail = user_data['useremail']

        self.database.execute('INSERT INTO users (name, user_email) VALUES ("'+ username +'", "'+ useremail +'")')
        self.database.commit()

        return 'User registered successfully.'
    
