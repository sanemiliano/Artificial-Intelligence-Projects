import numpy
import math

##Entrenamiento Positivo
EntrenamientoPositivo = open("train.positive.txt").read()
PalabrasAEncontrar = EntrenamientoPositivo.replace("\n","")
PalabrasAEncontrar = PalabrasAEncontrar.split(" ")
PalabrasUnicas = numpy.unique(PalabrasAEncontrar)
Oraciones = EntrenamientoPositivo.split("\n")
print("Texto leido y arreglos creados")

##Crear diccionario
Diccionario = {PalabrasUnicas[0]: 0}
for i in range(len(PalabrasUnicas)):
    Diccionario[PalabrasUnicas[i]] = i
print("Diccionario creado")

##Crear bolsa de palabras
BolsaDePalabras = [[0 for e in range(len(PalabrasUnicas))] for i in range(len(Oraciones))]
for i in range(len(Oraciones)):
    aux = Oraciones[i]
    aux = aux.split(" ")
    for e in range(len(aux)):
        if aux[e] is not '':
            BolsaDePalabras[i][Diccionario[aux[e]]] = 1
print("Bolsa de palabras creada")

##Obtener probabilidades
oracionesLen = len(Oraciones)
Probabilidades = [0 for i in range(len(PalabrasUnicas))]
probabilidadesLen = len(Probabilidades)

for i in range(probabilidadesLen):
    sum = 0
    for e in range(oracionesLen):
        sum += BolsaDePalabras[e][i]
    Probabilidades[i] = sum / len(Oraciones)

print("Probabilidades obtenidas")


##Entrenamiento Negativo
EntrenamientoNegativo = open("train.negative.txt").read()
PalabrasAEncontrar2 = EntrenamientoNegativo.replace("\n", "")
PalabrasAEncontrar2 = PalabrasAEncontrar2.split(" ")
PalabrasUnicas2 = numpy.unique(PalabrasAEncontrar2)
Oraciones2 = EntrenamientoNegativo.split("\n")
print("Texto leido y arreglos creados")

##Crear diccionario2
Diccionario2 = {PalabrasUnicas2[0]: 0}
for i in range(len(PalabrasUnicas2)):
    Diccionario2[PalabrasUnicas2[i]] = i
print("Diccionario2 creado")

##Crear bolsa de palabras
BolsaDePalabras2 = [[0 for e in range(len(PalabrasUnicas2))] for i in range(len(Oraciones2))]
for i in range(len(Oraciones2)):
    aux = Oraciones2[i]
    aux = aux.split(" ")
    for e in range(len(aux)):
        if aux[e] is not '':
            BolsaDePalabras2[i][Diccionario2[aux[e]]] = 1
print("Bolsa de palabras creada")

##Obtener probabilidades2
oraciones2Len = len(Oraciones2)
Probabilidades2 = [0 for i in range(len(PalabrasUnicas2))]
probabilidades2Len = len(Probabilidades2)

for i in range(probabilidades2Len):
    sum2 = 0
    for e in range(oraciones2Len):
        sum2 += BolsaDePalabras2[e][i]
    Probabilidades2[i] = sum2 / len(Oraciones2)

print("Probabilidades2 obtenidas")

Total = len(Oraciones) + len(Oraciones2)
probPos = len(Oraciones) / Total
probNeg = len(Oraciones2) / Total



##Prediccion/Pruebas positivas
PruebasPositivo = open("test.positive.txt").read()
OracionesPruebas = PruebasPositivo.split("\n")
print("Texto leido y arreglos creados")

oracionespruebaLen = len(OracionesPruebas)
sumatoriaLogPositivo = []
for i in range(oracionespruebaLen):
    aux = OracionesPruebas[i].split(" ")
    auxLen = len(aux)
    sumatoriaLogPositivo.append(0)
    for e in range(auxLen):
        if(aux[e] in Diccionario and Probabilidades[Diccionario[aux[e]]] > 0):
            sumatoriaLogPositivo[i] +=  math.log(probPos*Probabilidades[Diccionario[aux[e]]],2)

sumatoriaLogNegativa = []
for i in range(oracionespruebaLen):
    aux = OracionesPruebas[i].split(" ")
    auxLen = len(aux)
    sumatoriaLogNegativa.append(0)
    for e in range(auxLen):
        if (aux[e] in Diccionario2 and Probabilidades2[Diccionario2[aux[e]]] > 0):
            sumatoriaLogNegativa[i] +=  math.log(probNeg*Probabilidades2[Diccionario2[aux[e]]],2)

cont = 0
for i in range(oracionespruebaLen):
    if(sumatoriaLogPositivo[i] > sumatoriaLogNegativa[i]):
        cont += 1
print("El porcentaje de oraciones positivas clasificacadas correctamente es " + str(cont/oracionespruebaLen) )
print(cont)
print(oracionespruebaLen)


##Predicción/Pruebas negativo
PruebasNegativo = open("test.negative.txt").read()
OracionesPruebas1 = PruebasNegativo.split("\n")
print("Texto leido y arreglos creados")

oracionespruebaLen1 = len(OracionesPruebas1)
sumatoriaLogPositivo1 = []
for i in range(oracionespruebaLen1):
    aux = OracionesPruebas1[i].split(" ")
    auxLen = len(aux)
    sumatoriaLogPositivo1.append(0)
    for e in range(auxLen):
        if (aux[e] in Diccionario and Probabilidades[Diccionario[aux[e]]] > 0):
            sumatoriaLogPositivo1[i] += math.log(probPos*Probabilidades[Diccionario[aux[e]]], 2)

sumatoriaLogNegativa1 = []
for i in range(oracionespruebaLen1):
    aux = OracionesPruebas1[i].split(" ")
    auxLen = len(aux)
    sumatoriaLogNegativa1.append(0)
    for e in range(auxLen):
        if (aux[e] in Diccionario2 and Probabilidades2[Diccionario2[aux[e]]] > 0):
            sumatoriaLogNegativa1[i] += math.log(probNeg*Probabilidades2[Diccionario2[aux[e]]], 2)

cont = 0
for i in range(oracionespruebaLen1):
    if (sumatoriaLogPositivo1[i] < sumatoriaLogNegativa1[i]):
        cont += 1
print(cont)
print(oracionespruebaLen1)
print("El porcentaje de oraciones negativas clasificacadas correctamente es " + str(cont / oracionespruebaLen1))




