import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.stats as pearson

##Ejercicio 1
Y = pandas.read_csv('winequality-red.csv',sep = ";")
Y = Y.values
print(Y.shape)

##Un boxplot para cada una de las variables
FixedAcidity = Y[:,0]
plt.boxplot(FixedAcidity)
plt.plot([6],color='w', marker='*', markeredgecolor='k')
plt.show()

VolatileAcidity = Y[:,1]
plt.boxplot(VolatileAcidity)
plt.show()

CitricAcid = Y[:,2]
plt.boxplot(CitricAcid)
plt.show()

ResidualSugar = Y[:,3]
plt.boxplot(ResidualSugar)
plt.show()

Chlorides = Y[:,4]
plt.boxplot(Chlorides)
plt.show()

FreeSulfurDioxide = Y[:,5]
plt.boxplot(FreeSulfurDioxide)
plt.show()

TotalSulforDioxide = Y[:,6]
plt.boxplot(TotalSulforDioxide)
plt.show()

Density = Y[:,7]
plt.boxplot(Density)
plt.show()

pH = Y[:,8]
plt.boxplot(pH)
plt.show()

Sulphates = Y[:,9]
plt.boxplot(Sulphates)
plt.show()

Alcohol = Y[:,10]
plt.boxplot(Alcohol)
plt.show()

Quality = Y[:,11]
plt.boxplot(Quality)
plt.show()

##Un histograma de la ultima variable 12. quality
quality = Y[:,0]
plt.hist(quality)
plt.show()

##Una gráfica de dispersión de cada una de las variables contra
## la calidad (para visualizar dependencias). Indicar el coeficiente
# #de correlación de pearson entre cada par de variables.

print(pearson.pearsonr(quality,FixedAcidity))
plt.scatter(quality,FixedAcidity,label='Wine',color = 'k')
plt.xlabel('FixedAcidity')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,VolatileAcidity))
plt.scatter(quality,VolatileAcidity,label='Wine',color = 'k')
plt.xlabel('VolatileAcidity')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,CitricAcid))
plt.scatter(quality,CitricAcid,label='Wine',color = 'k')
plt.xlabel('CitricAcid')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,ResidualSugar))
plt.scatter(quality,ResidualSugar,label='Wine',color = 'k')
plt.xlabel('ResidualSugar')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,Chlorides))
plt.scatter(quality,Chlorides,label='Wine',color = 'k')
plt.xlabel('Chlorides')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,FreeSulfurDioxide))
plt.scatter(quality,FreeSulfurDioxide,label='Wine',color = 'k')
plt.xlabel('FreeSulfurDioxide')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,TotalSulforDioxide))
plt.scatter(quality,TotalSulforDioxide,label='Wine',color = 'k')
plt.xlabel('TotalSulfurDioxide')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,Density))
plt.scatter(quality,Density,label='Wine',color = 'k')
plt.xlabel('Density')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,pH))
plt.scatter(quality,pH,label='Wine',color = 'k')
plt.xlabel('pH')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,Sulphates))
plt.scatter(quality,Sulphates,label='Wine',color = 'k')
plt.xlabel('Sulphates')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

print(pearson.pearsonr(quality,Alcohol))
plt.scatter(quality,Alcohol,label='Wine',color = 'k')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Quality agaisnt other values')
plt.legend()
plt.show()

##* Una gráfica de boxplot de cada una de las variables pero separando
## los boxplot de acuerdo a la calidad.


##Ejercicio 2
X = pandas.read_csv('adult.csv',sep = ",")
X = X.values
print(X.shape)

## Una gráfica de barras o pastel por cada una de las
# variables categóricas.

Pais = list(X[:,13])
paises = numpy.unique(Pais)
cpaises = numpy.zeros( (len(paises)),int)

for p in range(len(paises)):
    cpaises[p] = Pais.count(paises[p])

plt.pie(cpaises, labels=paises)
plt.show()

Workclass = list(X[:,1])
workclasses = numpy.unique(Workclass)
cClasses = numpy.zeros( (len(workclasses)),int)

for p in range(len(workclasses)):
    cClasses[p] = Workclass.count(workclasses[p])

plt.pie(cClasses, labels=workclasses)
plt.show()

Education = list(X[:,3])
educations = numpy.unique(Education)
cEducations = numpy.zeros( (len(educations)),int)

for p in range(len(educations)):
    cEducations[p] = Education.count(educations[p])

plt.pie(cEducations, labels=educations)
plt.show()

MaritalStatus = list(X[:,5])
maritalstatuses = numpy.unique(MaritalStatus)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = MaritalStatus.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()

v7 = list(X[:,6])
maritalstatuses = numpy.unique(v7)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = v7.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()

v8 = list(X[:,7])
maritalstatuses = numpy.unique(v8)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = v8.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()


v9 = list(X[:,8])
maritalstatuses = numpy.unique(v9)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = v9.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()

v10 = list(X[:,9])
maritalstatuses = numpy.unique(v10)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = v10.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()

v13 = list(X[:,12])
maritalstatuses = numpy.unique(v13)
cMaritalStatuses = numpy.zeros( (len(maritalstatuses)),int)

for p in range(len(maritalstatuses)):
    cMaritalStatuses[p] = v13.count(maritalstatuses[p])

plt.pie(cMaritalStatuses, labels=maritalstatuses)
plt.show()

## Un boxplot para cada variable numérica.
Edad = X[:,0]
plt.boxplot(Edad)
plt.show()

Edad = X[:,2]
plt.boxplot(Edad)
plt.show()

Edad = X[:,10]
plt.boxplot(Edad)
plt.show()

Edad = X[:,11]
plt.boxplot(Edad)
plt.show()

Edad = X[:,1]
plt.boxplot(Edad)
plt.show()

##Una grafica que compare la variable de interés 15 (income) contra todas las demás varibles.
data = [[np.random.rand(100)] for i in range(3)]
plt.boxplot(data)
plt.xticks([1,2 , 3],['mon', 'tue', 'wed'])
plt.show()


##Histograma - edad
Edad = X[:,0]
plt.hist(Edad)
plt.show()