import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
df = pd.read_csv('mediumData.csv')
data = df['reading_time'].tolist()
fig = ff.create_distplot([data], ['reading_time'], show_hist = False)
fig.show()
print('population mean:- ',statistics.mean(data))
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex= random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ['reading_time'], show_hist = False)
    fig.show()
def setup():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(10)
        meanList.append(setOfMeans)
    showFig(meanList)
    print('sampling mean:- ', statistics.mean(meanList))
setup()