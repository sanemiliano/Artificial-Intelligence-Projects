import math
from random import randrange

import numpy
import matplotlib as plt
from PIL import Image


class Specimen:
    def __init__(self):
        self.Genes = numpy.random.randint(2, size=25)
        self.fitness = 0


def fromBinary(Array):
    base = 2
    result = 0
    for i in range(8):
        if(Array[i] == 1):
            result += base ** i
    return result

def binaryTournament(Specimens):
    contestant1 = Specimens[randrange(Population)]
    contestant2 = Specimens[randrange(Population)]
    if(contestant1.fitness <= contestant1.fitness):
        return contestant1
    else:
        return contestant2


def calculateFitness(Model,Specimen):
    enteroX = fromBinary(Specimen.Genes[0:8])
    enteroY = fromBinary(Specimen.Genes[8:16])
    enteroDegree = fromBinary(Specimen.Genes[16:25])
    enteroDegree *= enteroDegree * .0174533
    incX = ImageRangeX + resolution * (enteroX)
    incY = ImageRangeY + resolution * (enteroY)
    SpecimenRepresentation = transformacion(Model,incX,incY,enteroDegree)
    ny,nx = Model.shape
    modelCounter = 0
    SpecimenCounter = 0
    for ix in range(nx):
        for iy in range(ny):
            if Model[iy][ix] == 0:
                modelCounter += 1
                if SpecimenRepresentation[iy][ix] == 0:
                    SpecimenCounter += 1
    return modelCounter - SpecimenCounter

def transformacion (Img,incX,incY,teta):
    ny,nx = Img.shape
    teta_rad = teta * 0.0174533
    ImgT = numpy.ones((ny,nx),int)*255
    for ix in range(nx):
        for iy in range(ny):
            iy = int(iy)
            ix = int(ix)
            if Img[iy][ix] == 0:
                x = ix - nx / 2
                y = iy - ny / 2
                xx = x + incX
                yy = y + incY
                xxx = xx * math.cos(teta_rad) - yy * math.sin(teta_rad)
                yyy = xx * math.sin(teta_rad) + yy * math.cos(teta_rad)
                xxx = xxx + nx / 2
                yyy = yyy + ny / 2
                xxx = int(xxx)
                yyy = int(yyy)
                if yyy >= 0 and yyy < ny and xxx >=0 and xxx < nx:
                    ImgT[yyy,xxx] =  0
    return ImgT

IModelo = numpy.array(Image.open("Rectangulo.jpg"))
IModelo = IModelo[:,:,0]

Image.fromarray(IModelo).show()



#Parametros
Population = 100
Pm = .2
Pr = .6
nBits = 25
MaxIteration = 1000
ImageRangeX = -100
ImageRangeY = -75
resolution = (200) / ((2**8)-1)
#Poblacion
Specimens = [Specimen() for i in range(Population)]


#Calcular fitness
for i in range(Population):
    Specimens[i].fitness = calculateFitness(IModelo,Specimens[i])
print("Calculo de fitness termindo")

#Seleccion de elite
Elite = Specimens[0]
for i in range(Population):
    if (Specimens[i].fitness < Elite.fitness):
        Elite = Specimens[i]
#print(Specimens[0].Genes)
#print(Specimens[0].fitness)

counter = 0
currentFitness = 90000000000
Elite =  Specimen()
Elite.fitness = 90000000000
print("Comienzo de algoritmo")
while(counter < MaxIteration and currentFitness != 0):
    # Seleccion de nueva poblacion
    SelectedSpecimens = [Specimen() for i in range(Population)]
    for i in range(Population):
        SelectedSpecimens[i] = binaryTournament(Specimens)
    print("seleccion de nueva poblacion terminada")

    # Reproduccion
    BornedSpecimens = [Specimen() for i in range(Population)]
    for i in range(int(Population / 2)):
        father1 = SelectedSpecimens[randrange(Population)]
        father2 = SelectedSpecimens[randrange(Population)]
        son1 = Specimen()
        son2 = Specimen()
        if numpy.random.uniform(0, 1) <= Pr:
            separationIndex = numpy.random.randint(26)
            son1.Genes = numpy.concatenate((father1.Genes[:separationIndex], father2.Genes[separationIndex:]))
            son2.Genes = numpy.concatenate((father2.Genes[:separationIndex], father1.Genes[separationIndex:]))
            BornedSpecimens[i * 2] = son1
            BornedSpecimens[i * 2 + 1] = son2
        else:
            BornedSpecimens[i * 2] = father1
            BornedSpecimens[i * 2 + 1] = father2
    print("reproduccion terminada")

    #Mutacion
    for i in range(Population):
        if numpy.random.uniform(0, 1) <= Pm:
            index = numpy.random.randint(25)
            BornedSpecimens[i].Genes[index] = not (BornedSpecimens[i].Genes[index])
        Specimens[i] = BornedSpecimens[i]
    print("mutacion terminada")

    #Eligiendo el Elite
    for i in range(Population):
        Specimens[i].fitness = calculateFitness(IModelo, Specimens[i])
    anybetter = 0
    for i in range(100):
        if(Specimens[i].fitness < Elite.fitness):
            Elite = Specimens[i]
            anybetter = 1
    if anybetter == 0:
        Specimens[randrange(Population)] = Elite
    currentFitness =  Elite.fitness
    print("elite elegido y por graficar")
    enteroX = fromBinary(Elite.Genes[0:8])
    enteroY = fromBinary(Elite.Genes[8:16])
    enteroDegree = fromBinary(Elite.Genes[16:25])
    enteroDegree = enteroDegree * .0174533 #Conversion a radianes
    incX = ImageRangeX + resolution * (enteroX)
    incY = ImageRangeY + resolution * (enteroY)
    SpecimenRepresentation = transformacion(IModelo,incX,incY,enteroDegree)
    Image.fromarray(SpecimenRepresentation).show()




