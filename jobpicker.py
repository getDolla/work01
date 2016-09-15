#Yikai Wang and Farhan Haque

import random

def importCSV(fileName):
    inStream = open(fileName, 'r')
    lines = inStream.readlines()
    inStream.close()
    return lines

def cleanUp(L):
    for w in range(len(L)):
        L[w] = L[w].strip()
        L[w] = L[w].strip( "\n" )
        L[w] = L[w].strip( "\r" )
        if ('"' in L[w][0]):
            L[w] = L[w].split( '"' )[1:]
            L[w][1] = L[w][1][1:]
        else:
            L[w] = L[w].split( ',' )
    return L[1:len(L)-1]

def convertToDictionary(fileName):
    L = cleanUp(importCSV(fileName))
    #print L
    D = dict()
    for subL in L:
        #print subL
        #print ""
        D[subL[0]] = subL[1]
    return D

def randChooser(D):
    x = random.randrange(998)
    sumLast = 0
    
    for i in D:
        #print x
        #print float(D[i])*10
        #print sumLast
        sumLast = sumNow = sumLast + (float(D[i])*10)
        if ( x < sumNow ):
            return i

D = convertToDictionary("occupations.csv")
print D
print ""

for i in range(0, 10):
    print randChooser(D)
