
import numpy

#Parametros

Population = 100
Pr = .65
Pm = .3
MaxIteration = 10000

#Representación
class Specimen:
    def __init__(self):
        self.Genes = numpy.zeros((9,9),int)
        self.fitness = 0
        self.fixed = numpy.zeros((9,9),int)
        self.Genes = numpy.array(InitialConfiguration)
        aux = numpy.zeros((9),int)
        for e in range(9):
            aux = numpy.zeros((9), int)
            for z in range(9):
                if(self.Genes[e][z] != 0):
                    aux[self.Genes[e,z]-1] = 1
            for z in range(9):
                if (self.Genes[e,z] == 0):
                    index = 0
                    while(aux[index] == 1):
                        index += 1
                    aux[index] = 1
                    self.Genes[e,z] = index + 1


#Creacion de poblacion inicial
InitialConfiguration = [[1 ,0, 0, 0, 0, 7, 0, 9, 0],
                        [0 ,3 ,0 ,0 ,2 ,0 ,0 ,0 ,8],
                        [0 ,0 ,9 ,6 ,0, 0, 5, 0, 0],
                        [0 ,0 ,5 ,3 ,0 ,0 ,9 ,0 ,0],
                        [0, 1, 0 ,0, 8, 0, 0, 0, 2],
                        [6 ,0 ,0 ,0 ,0 ,4 ,0 ,0 ,0],
                        [3, 0, 0, 0 ,0 ,0 ,0, 1, 0],
                        [0 ,4 ,0 ,0 ,0 ,0 ,0 ,0 ,7],
                        [0, 0, 7, 0, 0, 0, 3, 0, 0]]

Specimens = [Specimen() for i in range(Population)]
print(Specimens[0].Genes)


#Calculo de la aptitud
def calculateFitness(Specimen):
    fitness = 0
    for i in range(9):
        aux = numpy.zeros((10),int)
        #Revisar por fila
        for e in range(9):
           if(aux[Specimen.Genes[i][e]]):
               fitness += 1
           else:
               aux[Specimen.Genes[i][e]] = 1
        aux = numpy.zeros((10), int)
        #Revisar por columna
        for e in range(9):
           if(aux[Specimen.Genes[e][i]]):
               fitness += 1
           else:
               aux[Specimen.Genes[e][i]] = 1
        #Revisar por cuadro
        for i in range(0,9,3):
            aux = numpy.zeros((10), int)
            for j in range(0,9,3):
                for k in range(0,3,1):
                    for l in range(0,3,1):
                        if (aux[Specimen.Genes[i+k][j+l]]):
                            fitness += 1
                        else:
                            aux[Specimen.Genes[i+k][j+l]] = 1
    return fitness

#Reproduccion
def reprodution(Specimen1,Specimen2):
    son = Specimen1
    if numpy.random.uniform(0, 1) <= Pr:
        for i in range(18):
            row = numpy.random.randint(9)
            column = numpy.random.randint(9)
            while(InitialConfiguration[row][column] > 0):
                row = numpy.random.randint(9)
                column = numpy.random.randint(9)
            son.Genes[row][column] = Specimen2.Genes[row][column]
    return son

#Mutacion
def mutation(Specimen1):
    if numpy.random.uniform(0, 1) <= Pm:
        for i  in range(9):
            row = numpy.random.randint(9)
            column = numpy.random.randint(9)
            row1 = numpy.random.randint(9)
            column1 = numpy.random.randint(9)
            while(InitialConfiguration[row][column] > 0):
                row = numpy.random.randint(9)
                column = numpy.random.randint(9)
            while(InitialConfiguration[row1][column1] > 0):
                row1 = numpy.random.randint(9)
                column1 = numpy.random.randint(9)
            aux = Specimen1.Genes[row][column]
            Specimen1.Genes[row][column] = Specimen1.Genes[row1][column1]
            Specimen1.Genes[row1][column1] = aux
    return Specimen1

#Torneo Binario
def binaryTournament(Specimens):
    contestant1 = Specimens[numpy.random.randint(Population)]
    contestant2 = Specimens[numpy.random.randint(Population)]
    if(contestant1.fitness <= contestant1.fitness):
        return contestant1
    else:
        return contestant2

# Ciclo Evolutivo
#Calcular fitness
for i in range(Population):
    Specimens[i].fitness = calculateFitness(Specimens[i])
print("Calculo de fitness termindo")


Elite = Specimens[0]
print(Elite.fitness)
for i in range(Population):
    if (Specimens[i].fitness < Elite.fitness):
        Elite = Specimens[i]

counter = 0
currentFitness = 90000000000

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
        father1 = SelectedSpecimens[numpy.random.randint(Population)]
        father2 = SelectedSpecimens[numpy.random.randint(Population)]
        if numpy.random.uniform(0, 1) <= Pr:
            BornedSpecimens[i * 2] = reprodution(father1,father2)
            BornedSpecimens[i * 2 + 1] = reprodution(father2,father1)
        else:
            BornedSpecimens[i * 2] = father1
            BornedSpecimens[i * 2 + 1] = father2
    print("reproduccion terminada")

    #Mutacion
    for i in range(Population):
        if numpy.random.uniform(0, 1) <= Pm:
            BornedSpecimens[i] = mutation(BornedSpecimens[i])
        Specimens[i] = BornedSpecimens[i]
    print("mutacion terminada")

    #Eligiendo el Elite
    for i in range(Population):
        Specimens[i].fitness = calculateFitness(Specimens[i])
    anybetter = 0
    for i in range(100):
        if(Specimens[i].fitness < Elite.fitness):
            Elite = Specimens[i]
            anybetter = 1
    if anybetter == 0:
        Specimens[numpy.random.randint(Population)] = Elite
    currentFitness =  Elite.fitness
    print(currentFitness)
