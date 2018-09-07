from PIL import Image
import numpy
from sklearn import neighbors, datasets
from scipy import ndimage
import scipy

images = ['106024.bmp','124080.bmp','153077.bmp','153093.bmp','181079.bmp','189080.bmp','208001.bmp','209070.bmp','21077.bmp','227092.bmp','24077.bmp','271008.bmp','304074.bmp','326038.bmp','37073.bmp','376043.bmp','388016.bmp','65019.bmp','69020.bmp','86016.bmp','banana1.bmp','banana2.bmp','banana3.bmp','book.bmp','bool.bmp','bush.bmp','ceramic.bmp','cross.bmp','doll.bmp','elefant.bmp','flower.bmp','fullmoon.bmp','grave.bmp','llama.bmp','memorial.bmp','music.bmp','person1.bmp','person2.bmp','person3.bmp','person4.bmp','person5.bmp','person6.bmp','person7.bmp','person8.bmp','scissors.bmp','sheep.bmp','stone1.bmp','stone2.bmp','teddy.bmp','tennis.bmp']

for image in images:
    print(image)
    ## Leer las imágenes
    Img = Image.open('images/'+image)
    Img_marcas = Image.open('bordes_mr/'+image)
    Img_real = Image.open('bordes_real/'+image)

    #Vectorizar las imágenes
    X = numpy.array(Img)
    nrows,ncols,nch = X.shape
    X = numpy.reshape(X,(nrows*ncols,3))
    Xm = numpy.reshape(numpy.array(Img_marcas),(nrows*ncols))
    Xr = numpy.reshape(numpy.array(Img_real),(nrows*ncols))

    ##KNN
    X0 = X[ Xm==255 ]
    X1 = X[ Xm==64 ]
    Y0 = numpy.ones( (len(X0)),int)*255
    Y1 = numpy.ones( (len(X1)),int)*0
    Xtrain = numpy.concatenate( (X0,X1) )
    Ytrain = numpy.concatenate( (Y0,Y1) )
    clf = neighbors.KNeighborsClassifier(5)
    clf.fit(Xtrain, Ytrain)
    Xp = clf.predict(X)

    Xp = numpy.reshape(Xp, (nrows, ncols))

    ##Erosion and Dilation
    for i in range(nrows):
        for e in range(ncols):
            if(Xp[i][e] == 255):
                Xp[i][e] = 1
    Xp = ndimage.binary_dilation(Xp).astype(Xp.dtype)
    Xp = ndimage.binary_erosion(Xp).astype(Xp.dtype)
    for i in range(nrows):
        for e in range(ncols):
            if(Xp[i][e] == 1):
                Xp[i][e] = 255


    ##BFS
    islands = [[0 for i in range(ncols)] for e in range(nrows)]
    countSize = 0
    countMarks = 0
    maxSize = 0
    maxMarkID = 0
    for i in range(nrows):
        for e in range(ncols):
            if (Xp[i][e] == 255 and islands[i][e] == 0):
                countMarks += 1
                islands[i][e] = countMarks
                countSize = 1
                sons = []
                sons.append((i, e))
                ##BFS
                while sons:
                    y, x = sons.pop(0)
                    up = True
                    down = True
                    left = True
                    right = True
                    if (x == 0):
                        left = False
                    if (y == 0):
                        up = False
                    if (x == ncols - 1):
                        right = False
                    if (y == nrows - 1):
                        down = False
                    if (up):
                        if (Xp[y - 1][x] == 255 and islands[y - 1][x] == 0):
                            sons.append((y - 1, x))
                            countSize += 1
                            islands[y - 1][x] = countMarks
                    if (down):
                        if (Xp[y + 1][x] == 255 and islands[y + 1][x] == 0):
                            sons.append((y + 1, x))
                            countSize += 1
                            islands[y + 1][x] = countMarks
                    if (right):
                        if (Xp[y][x + 1] == 255 and islands[y][x + 1] == 0):
                            sons.append((y, x + 1))
                            countSize += 1
                            islands[y][x + 1] = countMarks
                    if (left):
                        if (Xp[y][x - 1] == 255 and islands[y][x - 1] == 0):
                            sons.append((y, x - 1))
                            countSize += 1
                            islands[y][x - 1] = countMarks
                if (countSize > maxSize):
                    maxSize = countSize
                    maxMarkID = countMarks
    Xp = numpy.zeros((nrows,ncols),int)
    conti = 0
    for i in range(nrows):
        for e in range(ncols):
            if (islands[i][e] == maxMarkID):
                Xp[i][e] = 255
                conti += 1

    Img_pred = Xp
    Img_pred = Image.fromarray(Img_pred.astype(numpy.uint8))
    Img_pred.save('res/'+image,"BMP")
