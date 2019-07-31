import numpy as np
import matplotlib.pyplot as plt

# def sentpacketconvertbit(Inputlist):
#     binvalues = []
#     for i in range(len(Inputlist)):
#                 binaryValues=bin(int('1'+innerList[i], 16))[3:] 
#                 # split it by bits
#                 for x in binaryValues: 
#                     binvalues.append(x)
#     return binvalues

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




# THIS FUNCTION WORKS WELL
#reading from file
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
#per symbol
def getDiffrencesIndex(list1, list2):
    indecies = []
    for i in range(len(list1)):
        # print("list2[i],",list2[i])
        # print("list1[i],",list1[i])
        if list1[i] != list2[i]:
            indecies.append(i)

    return indecies

# THIS FUNCTION WORKS WELL
#PER SYMBOL It will return the indecices containing  errors
def ErrorIndices(ListSentPacket,ListErrorPatterns):
    indicesOferrors=[]
    # print("ListSentPacket",ListSentPacket)
    # print("ListErrorPatterns",ListErrorPatterns)
    for i in range(len(ListErrorPatterns)):
        # print("----List Error Patterns[i]",ListErrorPatterns[i])
        # print("----List sent packet",ListSentPacket)
        indices = getDiffrencesIndex(ListSentPacket[0], ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors

# THIS FUNCTION WORKS WELL
#number of Inner Errors in each symbol per generetion
#per symbol dar har symbol chand khata vujud darad=[1,3,4]:dar avali yeki dar dovomi 3ta dar sevomi 4 ta
def TotalBitFlipPerGeneration(ListSentPacket,ListErrorPatterns):
    numberofInnerErrors=[]
    for i in range(len(ListErrorPatterns)):
        count = getDiffrences(ListSentPacket[0], ListErrorPatterns[i])
        numberofInnerErrors.append(count)
    return numberofInnerErrors


#PER SYMBOL It will return the indecices containing  errors
def ErrorIndicesbit(ListSentPacket,ListErrorPatterns):
    indicesOferrors=[]
    for i in range(len(ListErrorPatterns)):
        indices = getDiffrencesIndex(sentPacket, ListErrorPatterns[i])
        indicesOferrors.append(indices)
    return indicesOferrors



sentPacket = [['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']]

recivedPack = [['52', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
              ,
              ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']   
             
             ,
              ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
              ]
#########################################PER BITS##################################################

sentPacketInBits=convertErrorPatternIntoBitGeneration(sentPacket)
# print("sentPacketInBits->",sentPacketInBits)
# print("len(sentPacketInBits)",len(sentPacketInBits)*8)

#remove the packets with  diffrent lengthes in bits
ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
# print("****************************" , ErrorPatternsinHexByte)

#convert all recieved packets into bits e.g.  '53'='0', '1', '0', '1', '0', '0', '1', '1'
ErrorPatternsinBinBit=convertErrorPatternIntoBitGeneration(ErrorPatternsinHexByte)
# print("ErrorPatternsinBinBit->",ErrorPatternsinBinBit)

#248 = 31*8
errorPatternSplitedBit=RemoveDifferentSize(ErrorPatternsinBinBit,248)
# print('len(errorPatternSplitedBit',len(errorPatternSplitedBit))
            
# THIS FUNCTION WORKS WELL
#Errors per symbol 
IndiciesOfError=ErrorIndices(sentPacketInBits,errorPatternSplitedBit) 
#print(indiciedoferror) will give :  [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 27, 28, 29, 30]]
print("IndiciesOfError->>>>",IndiciesOfError)


# THIS FUNCTION WORKS WELL
# #number of Inner Errors in each symbol per generetion
NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacketInBits,errorPatternSplitedBit)
print('NumberofInnerErrors,',NumberofInnerErrors)
#print(NumberofInnerErrors) will give :  [6, 9]


###############################PLOT##############################
def innerErrorDistributionCounter(AllErrorsByIndex):
    answer = []
    for i in range(31):
        answer.append(AllErrorsByIndex.count(i))

    return answer


def innerErrorDistributionPercentage(AllErrorsByIndex):
    answer = []
    for i in range(248):
        answer.append((float(AllErrorsByIndex.count(i)) /
                       float(len(AllErrorsByIndex)))*100)

    return answer

mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
x = []
# for i in range (len(numberofInnerErrors)):
#     x.append(i)


# density of inner errors

for i in range(248):
    x.append(i)

# the histogram of the data


# n = plt.bar(x,totalSpecificNumoferrors(numberofInnerErrors))
# plt.xlabel('#Inner errors')
# plt.ylabel('#Packets')


# innerErrorDistributionPercentage
# print(innerErrorDistributionPercentage(numberofInnerErrors))
# n = plt.bar(x,innerErrorDistributionPercentage(numberofInnerErrors))
# plt.title('Inner Error Distribution count')
# plt.xlabel('#Inner errors')
# plt.ylabel("#Packet")


# innerErrorDistributionPercentage
print(innerErrorDistributionPercentage(NumberofInnerErrors))
n = plt.bar(x, innerErrorDistributionPercentage(NumberofInnerErrors))
plt.title('Inner Error Distribution Percentage')
plt.xlabel('#Inner errors')
plt.ylabel("Packet Percentage")


# plt.xlabel('#Packet index ( in receiving order ) ')
# plt.ylabel('#Errors')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\sigma=15$')
plt.axis([0, 31, 0, 45])
plt.grid(True)
plt.show()