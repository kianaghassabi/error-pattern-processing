import string
import matplotlib.pyplot as plt
import numpy as np

# It works


def convertErrorPatternIntoBitGeneration(list):
    ''' Entery is list of all error patterns 
    and return each generation in bit rep
    so the answer will be a 2D list

    [
        [first bit of first generation ,  second bit of first generation, ... so on],
        [first bit of second generation ,  second bit of second generation, ... so on]
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
        [  [ [first bit of  first generation and first symbol],[],[] ],...],
        [  [ [first bit of secind generation and first symbol],[],[] ],...]
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
def readFromFile(fileaddress):
    '''
    pass the file address as a string, 
    it reads the file and split each generations data into array of  1 byte elements 
    You will receive a 2D array.
    '''
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
    '''
    Counts the number of different elements in two lists (Elemenet-wise)
    '''
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count

# THIS FUNCTION WORKS WELL
# per symbol


def getDiffrencesIndex(list1, list2):
    '''
    Returns the index of which two lists (inputs) have different elements
    '''
    indecies = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            indecies.append(i)

    return indecies

# function for removing elements with diffrent size


def RemoveDifferentSize(listOfElements, mysize):
    '''
    removes arrays from given 2D array (input) which they have different size form given size

    '''
    
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
    '''
    returns a 2D list of error indices due to Sentpacket (First parameter) over all given List of errror patterns

    '''
    indicesOferrors = []
    for i in range(len(ListErrorPatterns)):
        indices = getDiffrencesIndex(ListSentPacket[0], ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors

    # THIS FUNCTION WORKS WELL


# number of Inner Errors in each symbol per generetion
# per symbol dar har symbol chand khata vujud darad=[1,3,4]:dar avali yeki dar dovomi 3ta dar sevomi 4 ta
def TotalBitFlipPerGeneration(ListSentPacket, ListErrorPatterns):
    '''

    '''
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

# I've commented this section because maybe we need it for byte operations
# def innerErrorDistributionCounter(AllErrorsByIndex):
#     answer = []
#     for i in range(248):
#         answer.append(AllErrorsByIndex.count(i))
#     return answer


# def innerErrorDistributionPercentage(AllErrorsByIndex):
#     answer = []
#     print("AllErrorsByIndex in function for count",AllErrorsByIndex)
#     for i in range(248):
#         answer.append((float(AllErrorsByIndex.count(i)) /
#                        float(len(AllErrorsByIndex)))*100)
#     return answer

    
def innerErrorDistributionCounter(AllErrorsByIndex):
    '''
    give you the total error counts in specific index over all error patterns
    for instance, in the first bit over all error patterns we saw X number of errors
    '''
    answer = [ 0 for i in range (0,248)]
    for i in range (len(AllErrorsByIndex)): 
        for j in range(len(AllErrorsByIndex[i])):
            answer[AllErrorsByIndex[i][j]] +=1
    return answer


def innerErrorDistributionPercentage(AllErrorsByIndex):
    answer = []
    print("AllErrorsByIndex in function for count",AllErrorsByIndex)
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



###############################PLOT##############################
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