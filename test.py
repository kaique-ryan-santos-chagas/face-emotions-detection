import matplotlib.pyplot as plt
import pandas as pd
import os

data_path = os.path.join(os.getcwd(), 'data\\react_8eeaced1f2e0dfc753cc11e63b5abc12.csv')

dataframe = pd.read_csv(data_path)

for column in list(dataframe.columns):

    if column.find('box') == 0:
        del dataframe[column]




