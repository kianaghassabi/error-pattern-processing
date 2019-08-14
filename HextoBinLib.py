import string
import numpy as np

# THIS FUNCTION WORKS WELL
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

# THIS FUNCTION WORKS WELL
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
        # print("readline",readline)
        readline = readline.strip()
        line = readline.split(' ')
        # end of file
        if not readline:
            break
        # addding to the list of all errors so we would have a list conting other lists
        AllErrorPatterns.append(line)
    receivedPacketFile.close()
    #number of all
    print("len(AllErrorPatterns)",len(AllErrorPatterns))
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
    print("totalDiffrentlength:--->",totalDiffrentlength)
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
    Returns the number of (bit/Symbol) errors per symbol (if bit is considered) in each generation
    It will get a list of generation and will calculate this for all of them 
    for instance, [[1,3,4] , ...] 
    means in the first generation and first symbol we have 1 bit error 
    in the first generation and second symbol we have 3 bit errors
    '''
    numberofInnerErrors = []
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(ListSentPacket[0], ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


# #####################################BIT SPECIFIC OPERATIONS###########################################
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


def innerErrorDistributionCounterForBit(AllErrorsByIndex):
    '''
    give you the total error counts in specific index over all error patterns
    for instance, in the first bit over all error patterns we saw X number of errors
    '''
    answer = [0 for i in range(0, 248)]
    for i in range(len(AllErrorsByIndex)):
        for j in range(len(AllErrorsByIndex[i])):
            answer[AllErrorsByIndex[i][j]] += 1
    return answer


def innerErrorDistributionPercentageForBit(AllErrorsByIndex):
    '''
    returns you the percentage of error in specific index over all error patterns
    for instance, 30% of all first bit over all-error-patterns are errors 

    '''
    numberOfAllPacket = len(AllErrorsByIndex)
    answer = []
    answer = [0 for i in range(0, 248)]
    for i in range(len(AllErrorsByIndex)):
        for j in range(len(AllErrorsByIndex[i])):
            answer[AllErrorsByIndex[i][j]] += 1

    for i in range(0, 248):
        answer[i] = float(answer[i]) / float(numberOfAllPacket)
    return answer


def burstErrorCalculatorForBit(list):
    '''
    Shows the number of burst errors over all-error-patterns
    e.g., [0,10,11]
    0 error with length 0, 
    10 errors with lenght 1
    '''
    burstErrorData = [0 for i in range(0, 248)]

    for i in range(len(list)):
        continuousCounter = 1
        for j in range(1, len(list[i])):
            if(j == len(list[i]) - 1):
                if (list[i][j-1] + 1 == list[i][j]):
                    continuousCounter +=1
                    burstErrorData[continuousCounter] += 1
                    continuousCounter = 1
                else:
                    burstErrorData[continuousCounter] += 1
                    burstErrorData[1] += 1

            else: 
                if (list[i][j-1] + 1 == list[i][j]):
                    continuousCounter += 1
                else:
                    burstErrorData[continuousCounter] += 1
                    continuousCounter = 1
    return burstErrorData


def countTheErrorAverageForEachSymbol(list,numberOfErrorPatterns):
    '''
    receives count of errors for each indicies over all received error patterns 
    '''
    answer = []
    for i in range(0,int(len(list)/8)):
        temp = 0 
        for j in range(8):
            temp += list[(i*8)+j]
        answer.append(temp/numberOfErrorPatterns)

    return answer

