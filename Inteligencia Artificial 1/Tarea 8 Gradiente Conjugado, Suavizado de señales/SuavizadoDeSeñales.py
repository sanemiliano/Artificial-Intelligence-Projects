
import numpy
import math
import pandas
import matplotlib.pyplot as plt

e = .001

def Gradiente():
    result = numpy.zeros((sizee),float)
    for i in range(sizee):
        result[i] = Yc[i] - Yp[i]
        if(i > 0):
            result [i] += lamda * (Yc[i] - Yc[i-1])
        if(i < sizee-1):
            result [i] += lamda * (Yc[i] - Yc[i+1])
    return result

def Hessiano(Z):
    sizee = len(Z)
    result = numpy.zeros((sizee),float)
    for i in range(sizee):
        result[i] = Z[i]
        if i > 0 :
            result[i] += lamda * (Z[i] - Z[i-1])
        if i < sizee-1 :
            result[i] += lamda * (Z[i] - Z[i+1])
    return result

def obtenerDireccion(xk,funcion):
    return ((-Gradiente(funcion,xk))/math.sqrt(numpy.dot(Gradiente(funcion,xk),Gradiente(funcion,xk))))

def obtenerTamañoDePaso():
    return 0

def GradienteConjugado(xk):
    MaxIteraciones = 100
    gk = Gradiente()
    k = 0
    Pk = - gk
    alfaK = 0

    while(k < MaxIteraciones and math.sqrt(numpy.dot(gk,gk)) > e):
        alfak = (-numpy.dot(Pk,gk))/(numpy.matmul(Pk,Hessiano(Pk)))
        xk = xk + (alfak * Pk)
        gk1 = gk + alfak * Hessiano(Pk)
        Bk = (numpy.dot(gk1,gk1))/(numpy.dot(gk,gk))
        Pk1 = - gk1 + (Bk * Pk)
        k = k + 1

    return xk

D = pandas.read_csv('senial_ruido_1.csv')
D = D.values

Xp = D[:,0]
Xc = Xp
Yp = D[:,1]
Yc = Yp
sizee = len(Xp)
lamda = 1000

Yc = GradienteConjugado(Yp)

plt.plot(Xc,Yc)
plt.plot(Xp,Yp)
plt.show()
