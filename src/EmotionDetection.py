from fer import FER, Video

from src.database.DatabaseMethods import DatabaseMethods

import json

class EmotionDetection:

    def __init__(self, connection):

        self.detector = FER(mtcnn=True)
        self.database = DatabaseMethods(connection)
        

    def start_detection(self):

        pending_analyse = self.database.get_pending_analyse()

        print(pending_analyse)
        
        # video = Video('')
        # raw_data = video.analyze(self.detector) 

    
    def store_pending_analyse(self):

        print('Hello World!')



        
        


