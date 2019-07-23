import numpy as np
import matplotlib.pyplot as plt

# It works
def convertErrorPatternIntoBitGeneration(Inputlist):
    ''' Entery is list of all error patterns 
    and return each generation in bit rep
    so the answer will be a 2D list

    [
        [generation one: [first bit of first generation] , [ second bit of first generation], ... so on],
        [generation two: [first bit of second generation] , [ second bit of second generation], ... so on]
    ]

    '''
    errorPatternsInBitRep = [] 
    for innerList in Inputlist: 
        binvalues = []
        for i in range(len(innerList)):
            binaryValues=bin(int('1'+innerList[i], 16))[3:] 
             # split it by bits
            for x in binaryValues: 
                binvalues.append(x)
        errorPatternsInBitRep.append(binvalues)
    return errorPatternsInBitRep



# function for removing elements with diffrent size
def RemoveDifferentSize(listOfElements, mysize):
    newList = []
    totalDiffrentlength = 0
    for i in range(len(listOfElements)):
        sizeofElement = len(listOfElements[i])
        # print('size of elemnt:',sizeofElement,',','mysize:',mysize)
        if sizeofElement != mysize:
            #  listOfElements.remove(listOfElements[i])
            totalDiffrentlength += 1
        else:
            newList.append(listOfElements[i])
    # print('totalDiffrentlength',totalDiffrentlength)
    return newList


#reading from file
def readFromFile():
    # a list containing all errors
    AllErrorPatterns = []
    # open File
    receivedPacketFile = open("ReceivedPackets1.txt", "r")
    while True:
        # get line by line
        readline = receivedPacketFile.readline()
        readline = readline.strip()
        line = readline.split(' ')
        # end of file
        if not readline:
            break
        # addding to the list of all errors so we would have a list conting other lists
        AllErrorPatterns.append(line)
    receivedPacketFile.close()
    return AllErrorPatterns


# count the number of unmatched symbols
def getDiffrences(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count

#per symbol
def getDiffrencesIndex(list1, list2):
    indecies = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            indecies.append(i)

    return indecies

#per symbol
def ErrorIndices(ListSentPacket,ListErrorPatterns):
    indicesOferrors=[]
    for i in range(len(ListErrorPatterns)):
        indices = getDiffrencesIndex(sentPacket, ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors


#per symbol
def TotalBitFlipPerGeneration(ListSentPacket,ListErrorPatterns):
    numberofInnerErrors=[]
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(sentPacket, ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


# perbit
def getDiffrencesperbit(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count



#per bit :retunrs index per symbol
def getDiffrentIndices(list1, list2):
    indecies = []
    for i in range(len(list1)):
        index=[]
        for x in i:
            if list1[i][x] != list2[i][x]:
                index.append(x)
        indecies.append(index)
    return indecies

#per bit
def ErrorsIndices(ListSentPacket,ListErrorPatterns):
    indicesOferrors=[]
    for i in range(len(ListErrorPatterns)):
        indices = getDiffrencesIndices(sentPacket, ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors


#per bit
def TotalBitFlipPerGeneration(ListSentPacket,ListErrorPatterns):
    numberofInnerErrors=[]
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(sentPacket, ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


sentPacket = ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']

sentPacketInBits=convertErrorPatternIntoBitGeneration(sentPacket)
readfile=readFromFile()
ErrorPatternsinHexByte=RemoveDifferentSize(readfile,len(sentPacket))
ErrorPatternsinBinBit=convertErrorPatternIntoBitGeneration(ErrorPatternsinHexByte)
IndiciesOfError=ErrorIndices(sentPacket,ErrorPatternsinBinBit)
NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacket,ErrorPatternsinBinBit)

# print('NumberofInnerErrors,',NumberofInnerErrors)
print('IndiciesOfError',IndiciesOfError)