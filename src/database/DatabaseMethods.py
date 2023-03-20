import json

from datetime import date

class DatabaseMethods:

    def __init__(self, connection):

        self.database = connection


    def register_pending_analyse(self, user_email, file_name):

        date_today = date.today()
        
        self.database.execute('INSERT INTO pending_analyses (file_name, user_email, date_register) VALUES ("'+ file_name +'", "'+ user_email +'", "'+ str(date_today) +'") ')
        print('Analyse register sucessful.')

    
    def delete_pending_analyse(self, pending_analyse_id):

        self.database.execute('DELETE FROM pending_analyses WHERE id = ' + pending_analyse_id)
        print('Analyse removed sucessful.')

    
    def get_pending_analyse(self):

        pending_analyse = self.database.execute('SELECT * FROM pending_analyses LIMIT 1')

        analyse = json.dumps(pending_analyse.fetchall())

        return analyse
    
