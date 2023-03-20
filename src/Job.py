from src.EmotionDetection import EmotionDetection

class Job:

    def __init__(self):

        self.detector = EmotionDetection()
    
    def start_detection(self):

        self.detector.start_detection()

    def generate_report(self):

        print('Hello World')


