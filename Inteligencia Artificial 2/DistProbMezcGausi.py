from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier


#Tengo que agragar el alfa, un valor muy pequeño para que no sea 0.
import numpy
from PIL import Image
import math
from random import randint
from sklearn.mixture import GaussianMixture

imgs = [None] * 9
## Leer las imágenes
for i in range(9):
    imgs[i] = Image.open('ParaComparar/' + str(i)+'.jpg')
    imgs[i] = numpy.array(imgs[i])

for h in range(9):
    for g in range(9):
        ##Vectorizar las imagenes
        nrows1, ncols1, nch1 = imgs[g].shape
        nrows2, ncols2, nch2 = imgs[h].shape
        Ximg1 = numpy.reshape(imgs[g], (nrows1 * ncols1, nch1))
        Ximg2 = numpy.reshape(imgs[h], (nrows2 * ncols2, nch2))



        #Calcular la verosimilitud
        gmm1 = GaussianMixture(n_components=10, covariance_type='diag').fit(Ximg1)
        gmm2 = GaussianMixture(n_components=10, covariance_type='diag').fit(Ximg2)

        points1 = numpy.random.uniform(low=0, high=255, size=(1000, 3))
        probabilities1 = [0 for k in range(1000)]
        proba1 = gmm1.predict_proba(points1)  # regresa matriz de 10000x10
        for i in range(len(points1)):
            probabilities1[i] = numpy.dot(proba1[i], gmm1.weights_)

        points2 = numpy.random.uniform(low=0, high=255, size=(1000, 3))
        probabilities2 = [0 for k in range(1000)]
        proba2 = gmm2.predict_proba(points2)  # regresa matriz de 10000x10
        for i in range(len(points1)):
            probabilities2[i] = numpy.dot(proba2[i], gmm2.weights_)

        ##Calculamos la distacian entre las imagenes con la Divergencia Kullback Leibler
        KL1 = 0
        for i in range(1000):
            KL1 += probabilities1[i] * numpy.log(probabilities1[i]/probabilities2[i])
        KL2 = 0
        for i in range(1000):
            KL2 += probabilities2[i] * numpy.log(probabilities2[i]/probabilities1[i])

        print(str(h)+'vs' + str(g)+' '+str((KL1+KL2)/2))





