import os 

class Reports: 

    def __init__(self):

        self.message = 'Hello World'

    def generate_report(self, user_email):

        print('Sending report to: ', user_email)