import os 
import smtplib
import sqlite3 as database 
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import zipfile

from src.database.DatabaseMethods import DatabaseMethods as db

from jinja2 import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

class Reports: 

    def __init__(self, user_email, folder_name):
        
        self.useremail = user_email
        self.message = 'Emotions report.'
        self.template = ''
        self.connection = database.connect('face_emotion_detection.db')
        self.top_emotion = ''
        self.folder_name = folder_name
        self.video_drive_link = ''

        load_dotenv()

        self.generate_graphics()
        self.generate_report()

    
    def generate_graphics(self):

        data_path = os.path.join(os.getcwd(), 'data\\'+ self.folder_name +'\\'+ self.folder_name +'.csv')
        dataframe = pd.read_csv(data_path)
        dataframe = dataframe.dropna(axis=1, how='all')
        colors = mcolors.LinearSegmentedColormap.from_list("", ["#7B68EE", "#4B0082", "#8B008B"])

        count = 0

        for column in list(dataframe.columns):
            
            value = dataframe[column].isnull()
            
            if value[0] == True:
                del dataframe[column]   
                
                
        for column in list(dataframe.columns):
            
            if column.find('box') == 0:
                del dataframe[column]
            
            if column.find('happy') == 0:
                count = count + 1


        if count == 1:
            
            emotions = dataframe.columns
            
            happy = dataframe['happy0'].sum()
            sad = dataframe['sad0'].sum()
            angry = dataframe['angry0'].sum()
            neutral = dataframe['neutral0'].sum()
            fear = dataframe['fear0'].sum()
            disgust = dataframe['disgust0'].sum()
            surprise = dataframe['surprise0'].sum()
            
            values = [angry, disgust, fear, happy, neutral, sad, surprise]
            
            fig, axis = plt.subplots()
            
            bars = axis.bar(emotions, values)

            for i in range(len(bars)):
                bars[i].set_color(colors(i/len(bars)))
            
            for label in axis.get_xticklabels() + axis.get_yticklabels():
                label.set_color('#6959CD')
            
            axis.set_title('Emotions Graphic', color='#8A2BE2', weight='bold')
            axis.set_xlabel('Emotions', color='#8A2BE2', fontsize=14, weight='bold')
            axis.set_ylabel('Intensity', color='#8A2BE2', fontsize=14, weight='bold')
            
            axis.set_facecolor('black')
            fig.set_facecolor('black')
            
            save_graphic_path = os.path.join(os.getcwd(), 'data\\' + self.folder_name)
            
            plt.savefig(save_graphic_path + '\\emotions_graphic.png')
            
            max_intensity = max(happy, sad, angry, neutral, fear, disgust, surprise)

            for column in list(dataframe.columns):
                
                if dataframe[column].sum() == max_intensity:
                    
                    self.top_emotion = column[:-1]
                    print('The most intensity emotion is: ' + self.top_emotion)
            
            

    def generate_report(self):

        print('Generating report...')

        templates_path = os.path.join(os.getcwd(), 'src/templates')

        templates = templates_path.replace('/', '\\')

        with open(templates + '\\report-email.html', 'rb') as template_file:

            template = Template(template_file.read().decode('utf-8'))

        self.template = template

        with open(os.path.join(os.getcwd(), 'img/logo.png'), 'rb') as image_data:

           image = image_data.read()
        
        with open(os.path.join(os.getcwd(), 'data\\' + self.folder_name + '\\emotions_graphic.png'), 'rb') as image_data:

           emotions_graphic = image_data.read()

        logo_image = MIMEImage(image, name='logo.png')
        logo_image.add_header('Content-ID', '<logo>')

        emotions_image = MIMEImage(emotions_graphic, name='emotions_graphic.png')
        emotions_image.add_header('Content-ID', '<emotions_graphic>')

        self.message = MIMEMultipart()

        query = db(self.connection)

        user_data = query.get_user_data(self.useremail)

        if not user_data:
            print('User not found.')        
        else:

            username = user_data[0][1]
            html = self.template.render(username=username, top_emotion=self.top_emotion)
            self.message['From'] = 'artvibe.ai@gmail.com'
            self.message['To'] = self.useremail
            self.message['Subject'] = 'Your report is ready!'
            self.message.attach(logo_image)
            self.message.attach(emotions_image)
            self.message.attach(MIMEText(html, 'html'))
            
            print('Report is ready.')


    # Implement a function to send video analysed by AI to Google Drive and send the link to user because video can't be attached in the e-mail body.

    def send_video_google_drive(self):

        video = os.path.join(os.getcwd(), 'output\\' + self.folder_name + '_output.mp4')
        zip_path = os.path.join(os.getcwd(), 'output\\' + self.folder_name + '.zip')

        with zipfile.ZipFile(zip_path, 'w') as zip:
            zip.write(video, arcname=self.folder_name + '.mp4')
    
        # os.remove(video)


    def send_email(self):

        print('Sending e-mail...')

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('artvibe.ai@gmail.com', os.getenv('EMAIL_PASSWORD'))
        smtp_server.sendmail(self.message['From'], self.message['To'], self.message.as_string())
        smtp_server.quit()
        
        print('Email sent successfully.')

