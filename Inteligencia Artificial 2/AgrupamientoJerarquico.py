import numpy
import pandas
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

#Paso 1 Leer archivos
#1.1 Leer el nombre de las peliculas
peliculas = pandas.read_csv('Peliculas_descripcion.txt',sep ='|',header=None).values
peliculas = peliculas[:,1]

#1.2 Leer las calificaciones
registros = pandas.read_csv('Peliculas_Clientes.txt',sep = '\t',header=None).values
nPeliculas = 1682
nClientes = 943
calificaciones = numpy.zeros((nPeliculas,nClientes),float)
for r in registros:
        calificaciones[r[1]-1,r[0]-1] = r[2]

#Paso 2. Quedarse solo con las peliculas con mas de 300 valoraciones
evaluacionesPelicula = numpy.sum(calificaciones>0,axis=1)
idx = evaluacionesPelicula >= 100
indices = numpy.arange(nPeliculas)
indices = indices[idx]
print(indices)

#Paso 3. Calcular la similitud coseno entre las peliculas
def calculateCosineSimilarity(x,y):
    return numpy.dot(x,y)/numpy.sqrt(numpy.dot(x,x)*numpy.dot(y,y))

nPel = len(indices)
Similitudes = numpy.zeros((nPel,nPel),float)
for i in range(nPel):
    for e in range(nPel):
        Similitudes[i][e] = calculateCosineSimilarity(calificaciones[indices[e]][:],calificaciones[indices[i]][:])


#Paso 4. Mostrar el Dendrograma
#Cambiar a vectores unitarios los vectores de las peliculas
Z = linkage(calificaciones[indices,:],metric=calculateCosineSimilarity)
plt.figure()
dendrogram(Z,labels=indices+1)
plt.title('Dendogram: Peliculas')
plt.show()

for i in range(len(indices)):
    print(i,indices[i])

plt.figure(facecolor="white")
plt.imshow(Similitudes, cmap = 'hot', interpolation = 'nearest')
plt.title('matriz de distancias')
plt.colorbar()
plt.show()
