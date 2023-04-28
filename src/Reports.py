import os 
import smtplib
import sqlite3 as database 

from src.database.DatabaseMethods import DatabaseMethods as db

from jinja2 import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

class Reports: 

    def __init__(self, user_email):
        
        self.useremail = user_email
        self.message = 'Emotions report.'
        self.template = ''
        self.connection = database.connect('face_emotion_detection.db')

        load_dotenv()

        self.generate_report()

    def generate_report(self):

        print('Generating report...')

        templates_path = os.path.join(os.getcwd(), 'src/templates')

        templates = templates_path.replace('/', '\\')

        with open(templates + '\\report-email.html', 'rb') as template_file:

            template = Template(template_file.read().decode('utf-8'))

        self.template = template

        with open(os.path.join(os.getcwd(), 'img/logo.png'), 'rb') as image_data:

           image = image_data.read()

        logo_image = MIMEImage(image, name='logo.png')
        logo_image.add_header('Content-ID', '<logo>')

        self.message = MIMEMultipart()

        query = db(self.connection)

        user_data = query.get_user_data(self.useremail)

        if not user_data:
            print('User not found.')
        
        else:

            username = user_data[0][1]

            html = self.template.render(username=username)

            self.message['From'] = 'artvibe.ai@gmail.com'
            self.message['To'] = self.useremail
            self.message['Subject'] = 'Your report is ready!'
            self.message.attach(logo_image)
            self.message.attach(MIMEText(html, 'html'))
            
            print('Report is ready.')
            self.send_email()


    def send_email(self):

        print('Sending e-mail...')

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('artvibe.ai@gmail.com', os.getenv('EMAIL_PASSWORD'))
        smtp_server.sendmail(self.message['From'], self.message['To'], self.message.as_string())
        smtp_server.quit()
        
        print('Email sent successfully.')

