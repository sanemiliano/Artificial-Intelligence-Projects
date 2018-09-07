from ID3_DecisionTree import ID3_DecisionTree
import pandas
from PIL import Image
import numpy

X = [['No','Media','Excelente'],
     ['Si','Alta','Bueno'],
     ['No','Media','Bueno'],
     ['No','Baja','Bueno'],
     ['Si','Alta','Regular'],
     ['Si','Baja','Deficiente'],
     ['No','Media','Regular']]
Y = ['Excento','Excento','Final','Final','Final','Extraordinario','Extraordinario']
X = numpy.array(X)
Y = numpy.array(Y)

id3 = ID3_DecisionTree()
id3.fit(X,Y)
aux = X[:7,:]
print(id3.predict(aux))
print(id3.to_string())
