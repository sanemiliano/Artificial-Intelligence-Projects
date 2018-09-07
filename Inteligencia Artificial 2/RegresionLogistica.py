### Código base #################################################
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import sklearn.linear_model

image = 'flower.bmp'

## Leer las imágenes
Img = Image.open('images/'+image)
Img_marcas = Image.open('bordes_mr/'+image)
#Img.show()
#Img_marcas.show()
Img = numpy.array(Img)
Img_marcas = numpy.array(Img_marcas)

## Vectorizar las imágenes
nrows,ncols,nch = Img.shape
Ximg = numpy.reshape(Img,(nrows*ncols,nch))
Ximgm = numpy.reshape(Img_marcas,(nrows*ncols))
print(numpy.unique(Ximgm))

## Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Ximg[Ximgm==64,0], Ximg[Ximgm==64,1], Ximg[Ximgm==64,2], c='r', marker='*')
ax.scatter(Ximg[Ximgm==255,0],Ximg[Ximgm==255,1], Ximg[Ximgm==255,2], c='b', marker='o')
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
plt.show()

#Datos de entrenamiento
Xobj = Ximg[Ximgm==255,:]
Xfon = Ximg[Ximgm==64,:]
XX = numpy.concatenate((Xobj,Xfon))
Y = numpy.concatenate((numpy.ones(len(Xobj))*255,numpy.ones(len(Xfon))*64))

##Regresion Logistica
rl = sklearn.linear_model.LogisticRegression()
rl.fit(XX,Y)
nuevasMarcas = rl.predict(Ximg)
Image.fromarray(numpy.reshape(nuevasMarcas,(nrows,ncols))).show()



