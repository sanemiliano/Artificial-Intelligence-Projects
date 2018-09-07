import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.stats as pearson
import sklearn
import sklearn.linear_model

daysAhead = 3

Dataset = pandas.read_csv('HistoricalQuotes.csv',sep = ",")
DatasetTable = Dataset.values

x = []
for i in range(len(DatasetTable)):
    x.append(i)
x = numpy.array(x).reshape(-1,1)

y = DatasetTable[:,1]
model = sklearn.linear_model.LinearRegression()

model.fit(x,y)

x = numpy.zeros((479,11), float)

xPrediction = []
for i in range(len(DatasetTable),len(DatasetTable)+daysAhead):
    xPrediction.append(i)

xPrediction = numpy.array(xPrediction).reshape(-1,1)
results  = model.predict(xPrediction)

volatility = (y[0] - y[daysAhead])/y[daysAhead]

print(volatility)

print(results[len(results)-1] + (.447916 * volatility * y[0]))

