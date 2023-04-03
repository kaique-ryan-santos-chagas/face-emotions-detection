import os 
import smtplib

class Reports: 

    def __init__(self):

        self.message = 'Hello World'

    def generate_report(self):

        print('Generating report...')


    def send_email(self, user_email):

        print('Sending e-mail...')

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('kaique.github@gmail.com', 'mvhmmdgrwcctbdwx')

        from_addr = 'kaique.github@gmail.com'
        to_addr = 'kaique.chagas@globalhitss.com.br'
        subject = 'Your report is ready.'
        body = 'Visual Vibe'
        msg = f'Subject: {subject}\n\n{body}'

        smtp_server.sendmail(from_addr, to_addr, msg)

        smtp_server.quit()