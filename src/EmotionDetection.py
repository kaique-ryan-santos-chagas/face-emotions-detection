from fer import FER, Video

from src.database.DatabaseMethods import DatabaseMethods

import os

class EmotionDetection:

    def __init__(self, connection):

        self.detector = FER(mtcnn=True)
        self.database = DatabaseMethods(connection)
        

    def start_detection(self):

        pending_analyse = self.database.get_pending_analyse()

        if not pending_analyse:

            print('No review pending.')
        
        else:

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

            video.to_csv(raw_data, analyse_filename + '.csv')

            self.database.delete_pending_analyse(analyse_id)

    
    def store_pending_analyse(self):

        print('Hello World!')



        
        


