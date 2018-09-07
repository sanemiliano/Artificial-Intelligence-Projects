from ID3_DecisionTree import ID3_DecisionTree
import pandas
from PIL import Image
import numpy

def plot(X,i):
    Img = numpy.reshape(X[i,:]*255,(14,14))
    Img = Image.fromarray(Img.astype(numpy.uint8))
    Img.show()

def read_images(filename):
    X = pandas.read_csv(filename,header=None,sep=',').values
    D = numpy.zeros((len(X),196))
    for i,s in enumerate(X):
        D[i,:] = numpy.array(list(s[0])).astype(int)
    return D

Xtrain = read_images('DigitosPrueba/BD'+str(0)+'_train.txt')
Xtest = read_images('DigitosPrueba/BD'+str(0)+'_test.txt')
Ytrain = numpy.ones((5000,1))*0

Xtrain = []
Ytrain = []
Xtest = []

for i in range(4):
    Xtrain.append(read_images('DigitosPrueba/BD'+str(i)+'_train.txt'))
    Xtest.append(read_images('DigitosPrueba/BD'+str(i)+'_test.txt'))
    Ytrain.append(numpy.ones((5000,1))*i)

X = numpy.concatenate((Xtrain[0],Xtrain[1],Xtrain[2],Xtrain[3]),axis=0)
Y = numpy.concatenate((Ytrain[0],Ytrain[1],Ytrain[2],Ytrain[3]),axis=0)

clf = ID3_DecisionTree()
clf.fit(X,Y)

for i in range(10):
    prediction = clf.predict(Xtest[i])
    uI, cI = numpy.unique(prediction, return_counts=True)

