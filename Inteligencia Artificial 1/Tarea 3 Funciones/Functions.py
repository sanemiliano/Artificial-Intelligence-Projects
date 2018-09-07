import math
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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



def plot_3d(fun):
    Mat = numpy.arange(-5, 5, 0.1)
    XA = numpy.zeros((len(Mat) * len(Mat)), float)
    YA = numpy.zeros((len(Mat) * len(Mat)), float)
    ZA = numpy.zeros((len(Mat) * len(Mat)), float)
    i = 0
    for x in Mat:
        for y in Mat:
            arrX = numpy.array([x, y])
            z = fun(arrX)
            XA[i] = x
            YA[i] = y
            ZA[i] = z
            i = i + 1
    fig = plt.figure()
    image = fig.gca(projection='3d')
    image.plot_trisurf(XA, YA, ZA, linewidth=0.1, antialiased=True)
    plt.show()


def plot_2d(fun):
    X = numpy.arange(-5, 5, 0.1)
    n = X.size
    f = numpy.zeros((n,1))
    for i in range(n):
        f[i] = fun([X[i]])

    plt.plot(X, f, "r")
    plt.show()


plot_2d(Ackley)

plot_3d(Ackley)