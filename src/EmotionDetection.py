from fer import FER, Video

from src.database.DatabaseMethods import DatabaseMethods

import os
import zipfile
import json

class EmotionDetection:

    def __init__(self, connection):

        self.detector = FER(mtcnn=True)
        self.database = DatabaseMethods(connection)
        

    def start_detection(self):

        pending_analyse = self.database.get_pending_analyse()

        if pending_analyse:

            analyse_id = pending_analyse[0][0] 
            analyse_filename = pending_analyse[0][1]
            analyse_useremail = pending_analyse[0][2]
            analyse_date_register = pending_analyse[0][3]

            video_path_folder = os.path.join(os.getcwd(), 'videos')
            
            files = os.listdir(video_path_folder)

            for file in files:
                if os.path.isfile(os.path.join(video_path_folder, file)):  

                    filename, extension = os.path.splitext(file)

                    if filename == analyse_filename:

                        video_name = filename + extension
                        video_path = os.path.join(video_path_folder, video_name)

            video = Video(video_path)
            raw_data = video.analyze(self.detector)
            
            data_folder = os.path.join(os.getcwd(), 'data\\')
            
            os.mkdir(data_folder, analyse_filename) 

            data_path = os.path.join(os.getcwd(), 'data\\' + analyse_filename + '\\' + analyse_filename + '.csv')

            video.to_csv(raw_data, data_path)

            os.remove(os.getcwd() + '\\data.csv')

            self.database.delete_pending_analyse(analyse_id)

    
    def store_pending_analyse(self, data):

        video_data = json.loads(data)

        zip_files_path = os.path.join(os.getcwd(), 'zipfiles')
        video_files_path = os.path.join(os.getcwd(), 'videos')

        for filename in os.listdir(zip_files_path):

            filename_splited, extension = os.path.splitext(filename)

            if filename == video_data['filename'] + extension:

                filepath = os.path.join(zip_files_path, filename)

                if os.path.isfile(filepath):
                    with zipfile.ZipFile(filepath, 'r') as zip_ref:
                        zip_ref.extractall(video_files_path)


        self.database.register_pending_analyse(video_data)
                



        
        


