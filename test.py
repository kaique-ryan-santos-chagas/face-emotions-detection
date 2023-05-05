import os
import fer

detector = fer.FER(mtcnn=True)

image = os.path.join(os.getcwd(), 'img\\luna.jpg')
video = fer.Video(image)

raw_data = video.analyze(detector)

data_path = os.path.join(os.getcwd(), 'data\\luna.csv')

video.to_csv(raw_data, data_path)

os.remove(os.getcwd() + '\\data.csv')