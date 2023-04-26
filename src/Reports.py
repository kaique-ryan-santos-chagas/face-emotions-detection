import os 
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

class Reports: 

    def __init__(self):

        self.message = 'Emotions report.'

        templates_path = os.path.join(os.getcwd(), 'src/templates')

        templates = templates_path.replace('/', '\\')

        with open(templates + '\\report-email.html', 'rb') as template_file:

            template = template_file.read().decode('utf-8')

        self.template = template

        load_dotenv()

    def generate_report(self):

        print('Generating report...')


    def send_email(self, user_email):

        print('Sending e-mail...')

        with open(os.path.join(os.getcwd(), 'img/logo.png'), 'rb') as image_data:

           image = image_data.read()

        logo_image = MIMEImage(image, name='logo.png')
        logo_image.add_header('Content-ID', '<logo>')

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        smtp_server.login('artvibe.ai@gmail.com', os.getenv('EMAIL_PASSWORD'))

        message = MIMEMultipart()

        html = self.template

        message['From'] = 'artvibe.ai@gmail.com'
        message['To'] = user_email
        message['Subject'] = 'Your report is ready!'
        message.attach(logo_image)
        message.attach(MIMEText(html, 'html'))

        smtp_server.sendmail(message['From'], message['To'], message.as_string())

        smtp_server.quit()