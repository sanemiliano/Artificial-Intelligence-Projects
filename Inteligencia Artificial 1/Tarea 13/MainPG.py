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

def GeneticProgramming(X,Y):
    Pob = []
    symbols = [' + ', ' - ', ' * ', 'sin', 'cos', 'exp', 'abs']
    count = 0
    elite = None

    #Creo mi poblacion de 100 y guardo el Elite
    for i in range(0, 100):
        #Tomo una "variable" si la probabilidad es mayor al 0.5 si no, se toma "constante"
        if rd.random() > 0.5:
            Pob.append(Var(X,Y))
        else:
            Pob.append(Const(X,Y))

        # A este ultimo que fue el unico que ha cambiado le calculo el fitness, para compararlo con el elite y mejorarlo
        lastChanged = Pob[-1]
        lastChanged.calc_fitness(Y)
        if (elite == None) or (lastChanged.fitness < elite.fitness):
            elite = cp.copy(lastChanged)

    while count < 100000:
        # Eligo un simbolo al azar
        i = rd.randint(0, len(symbols) - 1)
        args = []
        # si el signo elegido es cualquiera de los primeros 4 (+, -, *, /) significa que recibe dos argumentos
        if i < 4:
            args.append(Pob[rd.randint(0, len(Pob) - 1)])

        # si no fue uno de los primeros 4, solo tomara un argumento
        args.append(Pob[rd.randint(0, len(Pob) - 1)])

        symbol = symbols[i]
        aux = Function(X,Y,symbol,args)

        #print(str(aux.fitness) +" <-> "+ str(elite.fitness))

        if aux.fitness < elite.fitness:
            elite = cp.copy(aux)

        #tomo otro simbolo al azar
        i = rd.randint(0, len(Pob) - 1)

        #Si el nuevo tiene mejor fitness se metera en el lugar del anterior
        if aux.fitness < Pob[i].fitness:
            Pob[i] = aux

        count += 1
    print("\nFuncion Elite Final-> ")
    print(elite.print())

####################################################
X = np.arange(-10, 10, 1)
Y = 9 + X**2
GeneticProgramming(X,Y)
print("\nFuncion original -> \n(9 + X**2)")
