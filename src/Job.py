from src.EmotionDetection import EmotionDetection

class Job:

    def __init__(self, connection):

        self.detector = EmotionDetection(connection)

    def run_scheduler(self):

        while True:
            self.start_detection()

    def start_detection(self):

        self.detector.start_detection()

  


