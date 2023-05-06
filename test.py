import matplotlib.pyplot as plt
import pandas as pd
import os

data_path = os.path.join(os.getcwd(), 'data\\react_8eeaced1f2e0dfc753cc11e63b5abc12.csv')

dataframe = pd.read_csv(data_path)

dataframe = dataframe.dropna(axis=1, how='all')

count = 0

for column in list(dataframe.columns):
    
    value = dataframe[column].isnull()
    
    if value[0] == True:
        del dataframe[column]   
        
    if column.find('happy') == 0:
        count = count + 1
        

print(dataframe.columns)


