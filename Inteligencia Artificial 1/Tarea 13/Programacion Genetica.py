import numpy as np
import copy as cp
import random as rd

class Node:
    def __init__(self):
        self.fitness = 0
        self.Yc = []

    def calc_fitness(self, Y):
        self.fitness = np.linalg.norm((self.Yc - Y))

    def print(self):
        pass

class Const(Node):
    def __init__(self, x, y):
        Node.__init__(self)
        self.value = rd.randint(-10, 10)
        self.Yc = np.ones((len(x)), float)*self.value
        self.calc_fitness(y)

    def print(self):
        return str(self.value)

class Var(Node):
    def __init__(self, x, y):
        Node.__init__(self)
        self.Yc = np.copy(x)
        self.calc_fitness(y)

    def print(self):
        return 'x'

class Function(Node):

    def __init__(self, X, Y, symbol, args):

        Node.__init__(self)
        self.symbol = symbol
        self.args = args

        if self.symbol == ' + ':
            self.Yc = self.args[0].Yc + self.args[1].Yc
        elif self.symbol == ' - ':
            self.Yc = self.args[0].Yc - self.args[1].Yc
        elif self.symbol == ' * ':
            self.Yc = self.args[0].Yc * self.args[1].Yc
        # elif self.symbol == '/':
            # self.Yc = self.args[0].Yc / self.args[1].Yc
        #elif self.symbol == ' / ':
         #  if(div == 0 ):
          #      self.Yc = 0
           # else:
            #    self.Yc = self.args[0].Yc / div
        elif self.symbol == 'sin':
            self.Yc = np.sin(self.args[0].Yc)
        elif self.symbol == 'cos':
            self.Yc = np.cos(self.args[0].Yc)
        # elif self.symbol == 'log':
            # self.Yc = numpy.log(self.args[0].Yc)
        #elif self.symbol == 'log':
         #   self.Yc = np.log(self.args[0].Yc)
        elif self.symbol == 'exp':
            self.Yc = np.exp(self.args[0].Yc)
        elif self.symbol == 'abs':
            self.Yc = np.abs(self.args[0].Yc)


        self.calc_fitness(Y)

    def print(self):
        if len(self.args) is 1:
            return self.symbol + ' ( '+ self.args[0].print()+' ) '
        else:
            return ' ( '+self.args[0].print() + self.symbol + self.args[1].print()+' ) '



#Código principal ***********************************
class GeneticProgramming:
    def __init__(self,X,Y):
        self.Pob = []
        self.symbols = [' + ', ' - ', ' * ', 'sin', 'cos', 'exp', 'abs']
        self.count = 0
        self.elite = None
        for i in range(0, 100):
            if rd.random() > 0.5:
                self.Pob.append(Var(X, Y))
            else:
                self.Pob.append(Const(X, Y))

            self.lastChanged = self.Pob[-1]
            self.lastChanged.calc_fitness(Y)
            if (self.elite == None) or (self.lastChanged.fitness < self.elite.fitness):
                self.elite = cp.copy(self.lastChanged)

    def fit(self,X,Y):
        while self.count < 100000:
            i = rd.randint(0, len(self.symbols) - 1)
            args = []
            if i < 4:
                args.append(self.Pob[rd.randint(0, len(self.Pob) - 1)])

            args.append(self.Pob[rd.randint(0, len(self.Pob) - 1)])

            symbol = self.symbols[i]
            aux = Function(X, Y, symbol, args)

            if aux.fitness < self.elite.fitness:
                self.elite = cp.copy(aux)

            i = rd.randint(0, len(self.Pob) - 1)
            if aux.fitness < self.Pob[i].fitness:
                self.Pob[i] = aux

            self.count += 1

    def print(self):
        print(self.elite.print())


X = np.arange(-10,10,1)
Y = X**2 - 4
gp = GeneticProgramming(X,Y)
gp.fit(X,Y)
gp.print()