import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.stats as sts
import math


def calculateProbability(X):
    options = numpy.unique(X)
    coptions = numpy.zeros((len(options)), float)
    for p in range(len(options)):
        coptions[p] = X.count(options[p])/len(X)
    return coptions

def calculateProbabilityXY(x,y,X,Y):
    probXY = 0.0
    for i in range(len(X)):
        if(X[i] == x and Y[i] == y):
            probXY += 1
    return (probXY/len(X))

def mutualInformation(X,Y):
    xUnique = list(numpy.unique(X))
    yUnique = list(numpy.unique(Y))
    xProbabilities = calculateProbability(X)
    yProbabilities = calculateProbability(Y)
    summ = 0.0
    for x in range(len(xUnique)):
        for y in range(len(yUnique)):
            probXY = calculateProbabilityXY(xUnique[x],yUnique[y],X,Y)
            if (probXY / (xProbabilities[x] * yProbabilities[y]) > 0):
                summ += probXY * math.log(probXY / (xProbabilities[x] * yProbabilities[y]),2)
    return summ

Y = pandas.read_csv('car.csv', header = None)
Y = Y.values
print(Y.shape)

varibles = []
for i in range(7):
    varibles.append(list(Y[:,i]))

for i in range(7):
    print(sts.entropy(calculateProbability(varibles[i]),None,2))

for i in range(7):
    for e in range(i,7):
        print(mutualInformation(varibles[i],varibles[e]))









