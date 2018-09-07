
import numpy
import math

def Sphere(arr):
    return numpy.dot(arr,arr)

def Rosenbrock(arr):
    sizee = len(arr)
    summ = 0
    for i in range(0, sizee-1):
        summ += 100*(arr[i+1] - arr[i]**2)**2 + (arr[i]-1)**2
    return summ

def Ackley(val):
    X = numpy.array(val)
    Scos = 0
    n = X.size
    Sx2 = numpy.dot( X,X )
    Scos = sum(numpy.cos( 2*math.pi*X ))

    fun = 20+math.exp(1)
    fun -= 20*math.exp( -0.2*math.sqrt((1/n*Sx2) ))
    fun -= math.exp( (1/n) *Scos )
    return fun


def Gradiente(funct,X):
    e = .01
    sizee = len(X)
    result = numpy.zeros((sizee),float)
    aux = numpy.zeros((sizee),float)
    for i in range(sizee):
        aux[i] = e
        result[i] = (funct(aux+X)-funct(X))/e
        aux[i] = 0
    return result

def Hessiano(funct,X):
    e = .01
    sizee = len(X)
    result = numpy.zeros((sizee,sizee),float)
    aux = numpy.zeros((sizee),float)
    for i in range(sizee):
        aux[i] = e
        result[i,:] = (Gradiente(funct,aux+X)-Gradiente(funct,X))/e
        aux[i] = 0
    return result

def GradientePorVector(funct,X,D):
    e = .1
    Xx = numpy.array(X)
    Dd= numpy.array(D)
    aux = Dd * e
    return (funct(aux+Xx)-funct(Xx))/e


def HessianoPorVector(funct,X,D):
    e = .1
    Xx = numpy.array(X)
    Dd = numpy.array(D)
    aux = Dd * e
    return ((Gradiente(funct,aux+Xx)-Gradiente(funct,Xx))/e)

arr = [2,3]
vec = [5,1]
print(HessianoPorVector(Sphere,arr,vec))