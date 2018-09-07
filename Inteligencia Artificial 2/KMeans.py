from sklearn.cluster import KMeans
import numpy
from PIL import Image

numpy.set_printoptions(threshold=numpy.inf)
image = 'lentes.jpg'

## Leer las imágenes
Img = Image.open('images/'+image)
Img.show()
Img = numpy.array(Img)

##Vectorizar las imagenes
nrows,ncols,nch = Img.shape
Ximg = numpy.reshape(Img,(nrows*ncols,nch))

##Agrupamiento K-Means
k = 3
kmeans = KMeans(n_clusters=k,).fit(Ximg)
clusters = kmeans.labels_
colors = [(66, 134, 244),(65, 244, 140),(235, 65, 244)]

#Pintar pixeles de cada grupo acorde al color de su centroide
for i in range(nrows*ncols):
    for e in range(k):
        if(clusters[i] == e):
            for y in range(nch):
                Ximg[i][y] = colors[e][y]

Image.fromarray(numpy.reshape(Ximg,(nrows,ncols,nch))).show()




