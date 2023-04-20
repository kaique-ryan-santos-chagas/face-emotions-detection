import os 
import smtplib

from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class Reports: 

    def __init__(self):

        self.message = 'Emotions report.'

        load_dotenv()

    def generate_report(self):

        print('Generating report...')


    def send_email(self, user_email):

        print('Sending e-mail...')

        templates_path = os.path.join(os.getcwd(), 'src/templates')

        env = Environment(loader=FileSystemLoader(templates_path.replace('/', '\\')))

        template = env.get_template('report-email.html')

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        smtp_server.login('artvibe.ai@gmail.com', os.getenv('EMAIL_PASSWORD'))

        html = template.render()

        message = MIMEMultipart()

        message['From'] = 'artvibe.ai@gmail.com'
        message['To'] = user_email
        message['Subject'] = 'Your report is ready!'
        message.attach(MIMEText(html, 'html'))

        smtp_server.sendmail(message['From'], message['To'], message.as_string())

        smtp_server.quit()