import pandas
import math
import numpy
import csv

#
# def getMutualInformation(X,Y):
#     MI = 0
#     for i in range(2):
#         Pi = P2(X,i)
#         for e in range(2):
#             JointProbability = P4(X,i,Y,e)
#             Pe = P2(Y,e)
#             if(Pe * Pi > 0 and JointProbability > 0):
#                 MI += JointProbability * math.log(JointProbability/(Pi * Pe),2)
#     return MI
#
# def P2(X,value):
#     counter = 0
#     for i in range(len(X)):
#         if(X[i] == str(value)):
#             counter += 1
#     return counter / len(X)
#
# def P4(X,valueX, Y,valueY):
#     counter = 0
#     for i in range(len(X)):
#         if(X[i] == str(valueX) and Y[i] == str(valueY)):
#             counter += 1
#     return counter / len(X)
#
#
#
# ##Creating Bayesian Nets from 0 to 3
# DataBases = []
# for a in range(1):
#
#     ##Reading information from data base
#     DataBases.append(pandas.read_csv("DigitosPrueba/BD"+str(a)+"_train.txt",header = None,sep=','))
#     print("Samples read")
#
#     ##Creating Mutual infomation table
#     MutualInformation = [[0 for i in range(196)] for e in range(196)]
#     #Creating CSV file with mutual information tble
#     # for i in range(196):
#     #     for e in range(i+1,196):
#     #         MutualInformation[i][e] = getMutualInformation(Samples[0][:][i],Samples[0][:][e])
#     #         MutualInformation[e][i] = MutualInformation[i][e]
#     # a = numpy.asarray(MutualInformation)
#     # numpy.savetxt("MutualInformationTable"+str(a)+".csv", a, delimiter=",")
#     ##Openinig file with CSV file of Mutual Information Table
#     MutualInformation = pandas.read_csv("MutualInformationTable"+str(a)+".csv",sep=",",header=None)
#     MutualInformation = MutualInformation.values
#     print("Mutual information table read")
#     #print("Mutual information table created")
#
#     ##Creating the Chou Lui Tree (Bayesian Net)
#     Fathers = [-1 for i in range(196)]
#     AlreadyInTree = []
#     HowManyChilds = [0 for i in range(196)]
#     UsedNodes = [0 for i in range(196)]
#
#         ##Choosing biggest mutual information between pixels, uning them creating the tree
#     max = 0
#     indexI = 0
#     indexE = 0
#     for i in range(196):
#         for e in range(i+1,196):
#             if(MutualInformation[i][e] > max):
#                 indexE = e
#                 indexI = i
#                 max = MutualInformation[i][e]
#
#     AlreadyInTree.append(indexI)
#     AlreadyInTree.append(indexE)
#     Fathers[indexE] = indexI
#     UsedNodes[indexI] = 1
#     UsedNodes[indexE] = 1
#
#         ##Add nodes to the tree until there is no more nodes to add
#     while(len(AlreadyInTree) < len(Fathers)):
#         max = 0
#         AlreadyInTreeL = len(AlreadyInTree)
#         for i in range(AlreadyInTreeL):
#                 for e in range(len(Fathers)):
#                     if(not UsedNodes[e]):
#                         if(MutualInformation[AlreadyInTree[i]][e] > max):
#                             indexE = e
#                             indexI = AlreadyInTree[i]
#                             max = MutualInformation[AlreadyInTree[i]][e]
#
#         AlreadyInTree.append(indexE)
#         Fathers[indexE] = indexI
#         UsedNodes[indexE] = 1
#
#     #Saving Chou Liu tree
#     numpy.savetxt("ChouLiuTree"+str(a)+".csv", Fathers)

##Predict data
def probabilityGivenThat(sample,i,e):
    #print("finding prob")
    Fathers = []
    place = e
    while (int(ChouLiuTrees[i][place][0]) != -1):
        #print(len(Fathers))
        Fathers.append([place, sample[place]])
        place = int(ChouLiuTrees[i][place][0])
    Fathers.append([place, sample[place]])
    #print("fathers obtained")
    countAll = 0
    countSpecific = 0
    a = Samples[0][0][Fathers[0][0]]
    g = Fathers[0][0]
    for j in range(len(sample)):
        det = True
        for w in range(len(Fathers)):
            if (Samples[i][j][Fathers[w][0]] != Fathers[w][1]):
                det = False
        if (det):
            countSpecific += 1
        det = True
        for w in range(1, len(Fathers)):
            if (Samples[i][j][Fathers[w][0]] != Fathers[w][1]):
                det = False
        if (det):
            countAll += 1
    return countSpecific / countAll


def predictEachProbability(probalities,sample):
    for i in range(len(probabilities)):
        sum = 0
        for e in range(len(sample)):
            #print("prob asked for")
            sum += probabilityGivenThat(sample,i,e)
            #print("One prob obtained")
        print(sum)
        probabilities[i] = sum
    index = 0
    max = 0
    for i in range(len(probabilities)):
        if(probabilities[i] > max):
            max = probabilities[i]
            index = i
    return i

    ##Reading ChouLiuTrees
ChouLiuTrees = []
for i in range(1):
    ChouLiuTrees.append(pandas.read_csv("ChouLiuTree"+str(i)+".csv",sep=",",header=None).values)

##Reading information from data base to predict

for i in range(1):
    Samples = pandas.read_csv("DigitosPrueba/BD" + str(0) + "_train.txt", header=None, sep=',')
    results = []
    SamplesT = pandas.read_csv("DigitosPrueba/BD"+str(0)+"_test.txt",header = None,sep=',')
    print("SamplesT read")
    for e in range(len(SamplesT)):
        probabilities = [0 for i in range(1)]
        results.append(predictEachProbability(probabilities,SamplesT[0][e]))
        numpy.savetxt("Results"+str(0)+".csv", results)
print("aloha")