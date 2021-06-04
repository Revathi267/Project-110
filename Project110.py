import statistics as st
import pandas as pd
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

population_mean = st.mean(data)

def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index = random.randint(0,counter)
        value = data[random_index]
        dataSet.append(value)
    mean_sample = st.mean(dataSet)
    return mean_sample    

def setUp():
    mean_list = []
    for i in range(0,100):
        set_of_means =  random_set_of_mean(30)
        mean_list.append(set_of_means)
    showFig(mean_list)


def showFig(mean_list):
    df = mean_list
    fig  =ff.create_distplot([df],["Reading Time"], show_hist=False)
    fig.show() 

setUp()
