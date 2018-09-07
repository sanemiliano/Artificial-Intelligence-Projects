from random import randrange, random

import numpy

def getFinesss(id):
    fit = 0
    for i in range(8):
        for j in range(i+1,8):
            if(i+1+specimens[id][i] == j+1+specimens[id][j]):
                fit += 1
            if(i+1-specimens[id][i] == j+1-specimens[id][j]):
                fit += 1
    return fit

def getFiness(toget,extra):
    fit = 0
    for i in range(8):
        for j in range(i+1,8):
            if(i+1+toget[i] == j+1+toget[j]):
                fit += 1
            if(i+1-toget[i] == j+1-toget[j]):
                fit += 1
    return fit

def binaryTournamentt():
    contestant1 = randrange(Population)
    contestant2 = randrange(Population)
    fit1 = getFinesss(contestant1)
    fit2 = getFinesss(contestant2)
    if(fit1 <= fit2):
        return contestant1
    else:
        return contestant2

def binaryTournament(one,two):
    fit1 = getFiness(one,1)
    fit2 = getFiness(two,1)
    if(fit1 <= fit2):
        return one
    else:
        return two

def reproduction(father1,father2):
    son = numpy.zeros((8),int)
    for i in range(4):
        son[i] = father1[i]
    for i in range(4,8):
        son[i] = father2[i]
    checked = numpy.zeros((8))
    for i in range(4):
        checked[son[i] - 1] = 1

    for i in range(4,8):
        if(checked[son[i]-1] == 1):
            for j in range(8):
                if(checked[j] == 0):
                    son[i] = j+1
                    checked[j] = 1
                    break
        else:
            checked[son[i]-1] = 1

    return son

def mutate(son):
    i = randrange(8)
    e = randrange(8)
    aux = son[i]
    son[i] = son[e]
    son[e] = aux
    return son

def replace(son):
    index = randrange(Population)
    opponent = specimens[index]
    specimens[index] = binaryTournament(son,opponent)
    return specimens[index]

def getMin(one,two):
    fit1 = getFiness(one,1)
    fit2 = getFiness(two,1)
    if(fit1 <= fit2):
        return one
    else:
        return two

Population = 100
specimens = numpy.zeros((Population,8),int)
specimensFitness = numpy.zeros((Population),int)

for i in range(Population):
    specimens[i] = numpy.arange(1,10,1,int)
    numpy.random.shuffle(specimens[i])

MutationProbability = .3
currentFitness = 90000000000
MaxIteration = 10000
k = 0

while(currentFitness != 0 and k < MaxIteration):
    father1 = specimens[binaryTournamentt()][:]
    father2 = specimens[binaryTournamentt()][:]
    son1 = reproduction(father1,father2)
    son2 = reproduction(father2,father1)
    if numpy.random.uniform(0,1) > MutationProbability :
        son1 = mutate(son1)
    if numpy.random.uniform(0,1) > MutationProbability :
        son2 = mutate(son2)
    replaced1 = replace(son1)
    replaced2 = replace(son2)
    stronger = getMin(replaced1,replaced2)
    currentFitness = getFiness(stronger,1)

print(stronger)

