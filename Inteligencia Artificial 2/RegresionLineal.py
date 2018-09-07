import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.stats as pearson
import sklearn
import sklearn.linear_model

Y = pandas.read_csv('.csv',sep = ";")
Y = Y.values
print(Y.shape)

x = numpy.zeros((1120,11), float)
y = numpy.zeros((1120),float)

for i in range(1120):
    for e in range(11):
        x[i,e] = Y[i,e]

for i in range(1120):
    y[i] = Y[i,11]

mysystem = sklearn.linear_model.LinearRegression()
mysystem.fit(x,y)

x = numpy.zeros((479,11), float)
for i in range(479):
    for e in range(11):
        x[i,e] = Y[i+1120,e]
print(mysystem.predict(x))