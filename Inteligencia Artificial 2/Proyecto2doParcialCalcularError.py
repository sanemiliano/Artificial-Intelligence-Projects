from PIL import Image
import numpy
from sklearn import neighbors, datasets

images = ['106024.bmp','124080.bmp','153077.bmp','153093.bmp','181079.bmp','189080.bmp','208001.bmp','209070.bmp','21077.bmp','227092.bmp','24077.bmp','271008.bmp','304074.bmp','326038.bmp','37073.bmp','376043.bmp','388016.bmp','65019.bmp','69020.bmp','86016.bmp','banana1.bmp','banana2.bmp','banana3.bmp','book.bmp','bool.bmp','bush.bmp','ceramic.bmp','cross.bmp','doll.bmp','elefant.bmp','flower.bmp','fullmoon.bmp','grave.bmp','llama.bmp','memorial.bmp','music.bmp','person1.bmp','person2.bmp','person3.bmp','person4.bmp','person5.bmp','person6.bmp','person7.bmp','person8.bmp','scissors.bmp','sheep.bmp','stone1.bmp','stone2.bmp','teddy.bmp','tennis.bmp']
error = []
for image in images:
    Img_pred = Image.open('res/' + image)
    Img_real = Image.open('bordes_real/' + image)

    # Vectorizar las imágenes
    Xp = numpy.array(Img_pred)
    nrows, ncols = Xp.shape
    Xp = numpy.reshape(Xp, (nrows * ncols))
    Xr = numpy.reshape(numpy.array(Img_real), (nrows * ncols))

    correctas = sum(numpy.logical_and(Xp==255,Xr==255))+sum(numpy.logical_and(Xp==0,Xr==0))
    incorrectas = sum(numpy.logical_and(Xp==0,Xr==255))+sum(numpy.logical_and(Xp==255,Xr==0))
    error.append( incorrectas/(correctas+incorrectas) )

print(len(error))
print(numpy.mean(error))