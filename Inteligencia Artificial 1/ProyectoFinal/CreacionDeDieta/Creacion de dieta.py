import random as rd
import copy as cp
class GeneticProgramming():
    def __init__(self,Goal):
        self.Pob = []
        self.possibleFood = []
        self.possibleFood.append(Food("Manzana",52))
        self.possibleFood.append(Food("Res magra de ternera", 95))
        self.possibleFood.append(Food("Sardina", 208))
        self.possibleFood.append(Food("Brocoli", 34))
        self.possibleFood.append(Food("Arroz", 111))
        self.possibleFood.append(Food("Spaguetti", 158))
        self.possibleFood.append(Food("Pera", 58))
        self.possibleFood.append(Food("Platano", 89))
        self.possibleFood.append(Food("Tortilla", 218))
        self.possibleFood.append(Food("Pollo", 239))
        self.possibleFood.append(Food("Zanahoria", 41))
        self.possibleFood.append(Food("Papa", 77))
        self.possibleFood.append(Food("Frijol", 108))
        self.possibleFood.append(Food("Huevo", 155))
        self.count = 0
        self.elite = None
        #Creación de mi población
        for i in range(0, 100):
            self.Pob.append(self.possibleFood[rd.randint(0, len(self.possibleFood) - 1)])

            self.lastChanged = self.Pob[-1]
            self.lastChanged.calc_Fitness(Goal)
            if (self.elite == None) or (self.lastChanged.fitness < self.elite.fitness):
                self.elite = cp.copy(self.lastChanged)

    def fit(self,Y):
        while self.count < 1000000 and self.elite.fitness >= 0:
            i = rd.randint(0, len(self.possibleFood) - 1)
            aux = cp.copy(self.possibleFood[i])
            e = rd.randint(0, len(self.Pob) - 1)
            aux.next = self.Pob[e]
            aux.accumulated += self.Pob[e].accumulated
            aux.calc_Fitness(Y)
            if aux.fitness < self.elite.fitness:
                self.elite = cp.copy(aux)

            i = rd.randint(0, len(self.Pob) - 1)
            if aux.fitness <= self.Pob[i].fitness:
                self.Pob[i] = aux

            self.count += 1

    def print(self):
        printe(self.elite)


class Food:

    def __init__(self,name,calories):
        self.fitness = 0
        self.next = None
        self.name = name
        self.calories = calories
        self.accumulated = calories
        self.id = id

    def calc_Fitness(self,Goal):
        self.fitness = Goal - self.accumulated

    def getCalories(self):
        return self.calories

    def getVitamins(self):
        return  self.vitamins

    def getMinerals(self):
        return self.minerals

    def getFat(self):
        return self.fat

    def __str__(self):
        return self.name + " " + str(self.calories)

    def __repr__(self):
        return str(self)

def printe(aux):
    print(aux.name + " "+str(aux.calories)+" "+str(aux.accumulated) + " "+ str(aux.fitness) )
    if(aux.next != None):
        printe(aux.next)


gp = GeneticProgramming(3000)
print(gp.Pob)
gp.fit(3000)
gp.print()

