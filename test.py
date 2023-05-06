import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import os


data_path = os.path.join(os.getcwd(), 'data\\react_8eeaced1f2e0dfc753cc11e63b5abc12\\react_8eeaced1f2e0dfc753cc11e63b5abc12.csv')
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
    
    save_graphic_path = os.path.join(os.getcwd(), 'data\\react_8eeaced1f2e0dfc753cc11e63b5abc12')
    
    plt.savefig(save_graphic_path + '\\emotions_graphic.png')
    
    max_intensity = max(happy, sad, angry, neutral, fear, disgust, surprise)

    for column in list(dataframe.columns):
        
        if dataframe[column].sum() == max_intensity:
            
            print('The most intensity emotion is: ' + column[:-1])
            
            