from PIL import Image
import numpy
from scipy.optimize import least_squares


def resize(I):
    n = len(I)
    n = int(n/2)
    I2 = numpy.zeros((n,n),float)
    for i in range(n):
        for j in range(n):
            I2[i,j]=(I[i*2,j*2]+I[i*2+1,j*2]+I[i*2,j*2+1]+I[i*2+1,j*2+1])/4
    return I2

def modelo(alpha,b1,b2,ndvi):
    baux = alpha[0] + (alpha[1]*b1 + alpha[2]*b2 + alpha[3]*(b1**2) + alpha[4]*(b2**2) + alpha[5]*b1*b2) * (1 + alpha[6]*ndvi + alpha[7]*ndvi**2)
    return baux

def error(alpha,b1,b2,ndvi,bi):
    bic = modelo(alpha,b1,b2,ndvi)
    return sum((bi-bic)**2)

B1 = numpy.array(Image.open('20120107.1729.t1.modis_cal_250_b1.tif'))
B2 = numpy.array(Image.open('20120107.1729.t1.modis_cal_250_b2.tif'))
b3 = numpy.array(Image.open('20120107.1729.t1.modis_cal_500_b3.tif'))
b4 = numpy.array(Image.open('20120107.1729.t1.modis_cal_500_b4.tif'))
b5 = numpy.array(Image.open('20120107.1729.t1.modis_cal_500_b5.tif'))
b6 = numpy.array(Image.open('20120107.1729.t1.modis_cal_500_b6.tif'))
b7 = numpy.array(Image.open('20120107.1729.t1.modis_cal_500_b7.tif'))

b1 = resize(B1)
b2 = resize(B2)

ndvi = (b2-b1) / (b1+b2)
NDVI = (B2-B1) / (B1+B2)

n = 100 * 100
b = numpy.concatenate((numpy.reshape(b1,(n,1)),numpy.reshape(b2,(n,1)),numpy.reshape(b3,(n,1)),numpy.reshape(b4,(n,1)),numpy.reshape(b5,(n,1)),numpy.reshape(b6,(n,1)),numpy.reshape(b7,(n,1)),numpy.reshape(ndvi,(n,1))),axis = 1)
N = 200 * 200

ls = least_squares(error,[0,0,0,0,0,0,0,0],args=[b[:,0],b[:,1],b[:,-1],b[:,3]])
alpha3 = ls.x
B3 = modelo(alpha3,numpy.reshape(B1,(N,1)),numpy.reshape(B2,(N,1)),numpy.reshape(NDVI,(N,1)))
B3 = numpy.reshape(B3,(200,200))

ls = least_squares(error,[0,0,0,0,0,0,0,0],args=[b[:,0],b[:,1],b[:,-1],b[:,4]])
alpha4 = ls.x
B4 = modelo(alpha4,numpy.reshape(B1,(N,1)),numpy.reshape(B2,(N,1)),numpy.reshape(NDVI,(N,1)))
B4 = numpy.reshape(B4,(200,200))

ls = least_squares(error,[0,0,0,0,0,0,0,0],args=[b[:,0],b[:,1],b[:,-1],b[:,5]])
alpha5 = ls.x
B5 = modelo(alpha3,numpy.reshape(B1,(N,1)),numpy.reshape(B2,(N,1)),numpy.reshape(NDVI,(N,1)))
B5 = numpy.reshape(B5,(200,200))

ls = least_squares(error,[0,0,0,0,0,0,0,0],args=[b[:,0],b[:,1],b[:,-1],b[:,6]])
alpha6 = ls.x
B6 = modelo(alpha3,numpy.reshape(B1,(N,1)),numpy.reshape(B2,(N,1)),numpy.reshape(NDVI,(N,1)))
B6 = numpy.reshape(B6,(200,200))

ls = least_squares(error,[0,0,0,0,0,0,0,0],args=[b[:,0],b[:,1],b[:,-1],b[:,7]])
alpha7 = ls.x
B7 = modelo(alpha3,numpy.reshape(B1,(N,1)),numpy.reshape(B2,(N,1)),numpy.reshape(NDVI,(N,1)))
B7 = numpy.reshape(lB7,(200,200))

Image.fromarray(b3).show()
Image.fromarray(B3).show()

Image.fromarray(b4).show()
Image.fromarray(B4).show()

Image.fromarray(b5).show()
Image.fromarray(B5).show()

Image.fromarray(b6).show()
Image.fromarray(B6).show()

Image.fromarray(b7).show()
Image.fromarray(B7).show()






