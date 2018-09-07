from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import numpy
from PIL import Image
import math

numpy.set_printoptions(threshold=numpy.inf)

image = 'flower.bmp'

## Leer las imágenes
Img = Image.open('images/'+image)
Img_marcas = Image.open('bordes_mr/'+image)
Img = numpy.array(Img)
Img_marcas = numpy.array(Img_marcas)
print(Img_marcas)

##Vectorizar las imagenes
nrows,ncols,nch = Img.shape
Ximg = numpy.reshape(Img,(nrows*ncols,nch))
Ximgm = numpy.reshape(Img_marcas,(nrows*ncols))

##Agrupamiento K-Means
k = 20
kmeans = KMeans(n_clusters=k,).fit(Ximg)
clusters = kmeans.labels_
centroids = kmeans.cluster_centers_
colors = [(66, 134, 244),(65, 244, 140),(235, 65, 244)]

#Cambiar el espacio de los datos (pixeles) de 3D (rgb)
# a 20D usando la función kernel Gaussiano con las similitudes de los pixeles a cada uno de los centroides
# obtenidos en kmeans.
newDimensions = numpy.zeros((nrows*ncols,k), float)
for i in range(nrows*ncols):
    for e in range(20):
        a = Ximg[i][:]
        b = centroids[e][:]
        c = a - b
        newDimensions[i][e] = numpy.exp(-numpy.sqrt(numpy.dot(c,c))/2)

# Datos de entrenamiento
Xobj = newDimensions[Ximgm == 255, :]
Xfon = newDimensions[Ximgm == 64, :]
XX = numpy.concatenate((Xobj, Xfon))
Y = numpy.concatenate((numpy.ones(len(Xobj)) * 255, numpy.ones(len(Xfon)) * 64))

##Vecino Mas Cercano (Nearest neighbour
rl = KNeighborsClassifier()
rl.fit(XX, Y)
nuevasMarcas = rl.predict(newDimensions)
Image.fromarray(numpy.reshape(nuevasMarcas, (nrows, ncols))).show()





