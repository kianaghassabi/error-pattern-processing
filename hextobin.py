import string
import matplotlib.pyplot as plt
import numpy as np

# It works


def convertErrorPatternIntoBitGeneration(list):
    ''' Entery is list of all error patterns 
    and return each generation in bit rep
    so the answer will be a 2D list

    [
        [generation one: [first bit of first generation] , [ second bit of first generation], ... so on],
        [generation two: [first bit of second generation] , [ second bit of second generation], ... so on]
    ]

    '''
    errorPatternsInBitRep = []
    counter = 0
    for innerList in list:
        counter += 1
        # print(counter)
        binvalues = []
        for i in range(len(innerList)):
            binaryValues = bin(int('1'+innerList[i], 16))[3:]
            # split it by bits
            for x in binaryValues:
                binvalues.append(x)
        errorPatternsInBitRep.append(binvalues)
    return errorPatternsInBitRep


# It also works fine
def convertErrorPatternIntoBitSymbol(list):
    ''' 
    Entery is list of all error patterns 
    and return each symbol in another list in bit rep
    also puts all symbols lists into another list 
    so the answer will be a 3D list
    [
        [ generation one [ symbol one [first bit of first symbol],[],[] ],...],
        [ generation two [ symbol one [first bit of first symbol],[],[] ],...]
    ]

    '''
    errorPatternsInBitRep = []
    for innerList in list:
        binvalues = []
        for i in range(len(innerList)):
            binaryValues = bin(int('1'+innerList[i], 16))[3:]
            # split it by bits
            binvalues.append([x for x in binaryValues])
        errorPatternsInBitRep.append(binvalues)
    return errorPatternsInBitRep


# THIS FUNCTION WORKS WELL
# reading from file
def readFromFile(fileaddress):
    # a list containing all errors
    AllErrorPatterns = []
    # open File
    receivedPacketFile = open(fileaddress, "r")
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

# THIS FUNCTION WORKS WELL
# count the number of unmatched symbols


def getDiffrences(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count

# THIS FUNCTION WORKS WELL
# per symbol


def getDiffrencesIndex(list1, list2):
    indecies = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            indecies.append(i)

    return indecies

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

# THIS FUNCTION WORKS WELL
# PER SYMBOL It will return the indecices containing  errors


def ErrorIndices(ListSentPacket, ListErrorPatterns):
    indicesOferrors = []
    for i in range(len(ListErrorPatterns)):
        indices = getDiffrencesIndex(ListSentPacket[0], ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors

    # THIS FUNCTION WORKS WELL


# number of Inner Errors in each symbol per generetion
# per symbol dar har symbol chand khata vujud darad=[1,3,4]:dar avali yeki dar dovomi 3ta dar sevomi 4 ta
def TotalBitFlipPerGeneration(ListSentPacket, ListErrorPatterns):
    numberofInnerErrors = []
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(ListSentPacket[0], ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


# THIS FUNCTION WORKS WELL
# PER SYMBOL It will return the indecices containing  errors
def ErrorIndicesforbits(ListSentPacket, ListErrorPatterns):
    indicesOferrors = []
    # print("ListSentPacket",ListSentPacket)
    # print("ListErrorPatterns",ListErrorPatterns)
    for i in range(len(ListErrorPatterns)):
        # print("----List Error Patterns[i]",ListErrorPatterns[i])
        # print("----List sent packet",ListSentPacket)
        indices = getDiffrencesIndex(ListSentPacket[0], ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors

# THIS FUNCTION WORKS WELL
# number of Inner Errors in each symbol per generetion
# per symbol dar har symbol chand khata vujud darad=[1,3,4]:dar avali yeki dar dovomi 3ta dar sevomi 4 ta


def TotalBitFlipPerGenerationforbits(ListSentPacket, ListErrorPatterns):
    numberofInnerErrors = []
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(ListSentPacket[0], ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


###############################PLOT##############################
def innerErrorDistributionCounter(AllErrorsByIndex):
    answer = []
    for i in range(248):
        answer.append(AllErrorsByIndex.count(i))
    return answer


def innerErrorDistributionPercentage(AllErrorsByIndex):
    answer = []
    print("AllErrorsByIndex in function fopr count",AllErrorsByIndex)
    for i in range(248):
        answer.append((float(AllErrorsByIndex.count(i)) /
                       float(len(AllErrorsByIndex)))*100)
    return answer

# def innerErrorDistributionPercentage(AllErrorsByIndex):
#     answer = []
#     print("AllErrorsByIndex in function fopr count", AllErrorsByIndex)
#     for j in range(len(AllErrorsByIndex)):
#         for i in range(248):
#             answer.append((float(AllErrorsByIndex[j].count(i)) /
#                            float(len(AllErrorsByIndex[j])))*100)
#     return answer



def Plot(numberOfBits,ListofInnerErrors,PlotTitle,plotXLabel,pltYLabel,XrangeFrom,XrangeTo,YrangeFrom,YrangeTo):
    # initilizing
    # mu = InputMu
    # sigma = InputSimga


    x = []
    for i in range(numberOfBits):
        x.append(i)

    # innerErrorDistributionPercentage
    print(innerErrorDistributionPercentage(ListofInnerErrors))
    plt.bar(x,innerErrorDistributionPercentage(ListofInnerErrors)) 
    plt.title(PlotTitle)
    plt.xlabel(plotXLabel)
    plt.ylabel(pltYLabel)

    plt.axis([XrangeFrom, XrangeTo, YrangeFrom, YrangeTo])
    plt.grid(True)
    plt.show()
