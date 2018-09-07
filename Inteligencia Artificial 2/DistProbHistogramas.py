from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier


#Tengo que agragar el alfa, un valor muy pequeño para que no sea 0.
import numpy
from PIL import Image
import math

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

        ##Contamos
        axis = [None] * 3

        counter = [[[0 for k in range(5)]for j in range(5)]for i in range(5)]
        for i in range(5):
            for e in  range(5):
                for j in range(5):
                    counter[i][e][j] = 1

        for i in range(ncols1 * nrows1):
            for e in range(3):
                if (Ximg1[i][e] < 52):
                    axis[e] = 0
                else:
                    if (Ximg1[i][e] <103):
                        axis[e] = 1
                    else:
                        if (Ximg1[i][e] < 154):
                            axis[e] = 2
                        else:
                            if (Ximg1[i][e] < 205):
                                axis[e] = 3
                            else:
                                axis[e] = 4
            counter[axis[0]][axis[1]][axis[2]] = counter[axis[0]][axis[1]][axis[2]] +1

        probabilities1 = [[[0 for k in range(5)]for j in range(5)]for i in range(5)]

        for i in range(5):
            for e in  range(5):
                for j in range(5):
                    probabilities1[i][e][j] = counter[i][e][j] / (nrows1 * ncols1)

        for i in range(5):
            for e in  range(5):
                for j in range(5):
                    counter[i][e][j] = 1

        for i in range(ncols2* nrows2):
            for e in range(3):
                if (Ximg2[i][e] < 52):
                    axis[e] = 0
                else:
                    if (Ximg2[i][e] <103):
                        axis[e] = 1
                    else:
                        if (Ximg2[i][e] < 154):
                            axis[e] = 2
                        else:
                            if (Ximg2[i][e] < 205):
                                axis[e] = 3
                            else:
                                axis[e] = 4
            counter[axis[0]][axis[1]][axis[2]] = counter[axis[0]][axis[1]][axis[2]] +1

        probabilities2 = [[[0 for k in range(5)] for j in range(5)]for i in range(5)]

        for i in range(5):
            for e in  range(5):
                for j in range(5):
                    probabilities2[i][e][j] = counter[i][e][j] / (ncols2*nrows2)

        ##Calculamos la distacian entre las imagenes con la Divergencia Kullback Leibler
        KL1 = 0
        for i in range(5):
            for e in range(5):
                for j in range(5):
                        KL1 += probabilities1[i][e][j] * math.log((probabilities1[i][e][j]/probabilities2[i][e][j]))

        KL2 = 0
        for i in range(5):
            for e in range(5):
                for j in range(5):
                        KL2 += probabilities2[i][e][j] * math.log((probabilities2[i][e][j]/probabilities1[i][e][j]))

        print(str(h)+'vs' + str(g)+' '+str((KL1+KL2)/2))






