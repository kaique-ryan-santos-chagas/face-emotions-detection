from fer import FER, Video

from database.DatabaseMethods import DatabaseMethods

class EmotionDetection:

    def __init__(self):

        self.detector = FER(mtcnn=True)
        self.database = DatabaseMethods()
        

    def start_detection(self):

        pending_analyse = self.database.get_pending_analyse()
        
        print(pending_analyse)

        # video = Video('')
        # raw_data = video.analyze(self.detector) 

    
    def store_pending_analyse(self):

        print('Hello World!')



        
        


