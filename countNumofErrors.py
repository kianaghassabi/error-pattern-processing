import numpy as np
import matplotlib.pyplot as plt

from hextobin import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol

# a list containing all errors
AllErrorPatterns = []

# open File
receivedPacketFile = open("ReceivedPackets1.txt", "r")
counter = 0 
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

print(AllErrorPatterns[4407])
GenerationsBit = IntoBitGeneration(AllErrorPatterns)
# inner erros


def innerErrorDistributionCounter(AllErrorsByIndex):
    answer = []
    for i in range(31):
        answer.append(AllErrorsByIndex.count(i))

    return answer


def innerErrorDistributionPercentage(AllErrorsByIndex):
    answer = []
    for i in range(31):
        answer.append((float(AllErrorsByIndex.count(i)) /
                       float(len(AllErrorsByIndex)))*100)

    return answer


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

# count the number of unmatched symbols


def getDiffrences(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    # print(count)
    return count


def getDiffrencesIndex(list1, list2):

    indecies = []

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            indecies.append(i)

    # print(count)
    return indecies


def burstErrorCalculator(list):

    burstErrorData = []
    for i in range(31):
        burstErrorData.append(0)

    for i in range(len(list)):
        continuousCounter = 0
        for j in range(1, len(list[i])):
            if (list[i][j-1] + 1 == list[i][j]):
                continuousCounter += 1
            else:
                burstErrorData[continuousCounter] += 1
                continuousCounter = 0
    return burstErrorData


sentPacket = ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']

# 53 == > bit
lenghthsSentPacket = len(sentPacket)
# print('lenghthsSentPacket',lenghthsSentPacket)
# remove diffrent size errors

# for i in range(50):
#     print("::::::",len(AllErrorPatterns[i]),"::::::")


allRemoved = RemoveDifferentSize(AllErrorPatterns, lenghthsSentPacket)

# numberofErrors in each received packet
numberofInnerErrors = []

indicesOferrors = []

for i in range(len(allRemoved)):
    # testlen=[3,2]
    # print('testlen',len(testlen))
    count = getDiffrences(sentPacket, allRemoved[i])
    indices = getDiffrencesIndex(sentPacket, allRemoved[i])

    indicesOferrors.append(indices)
    # print(allRemoved[i])
    # print('count',count)
    numberofInnerErrors.append(count)
# print(numberofInnerErrors)


burstErrorData = burstErrorCalculator(indicesOferrors)


mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
x = []
# for i in range (len(numberofInnerErrors)):
#     x.append(i)


# density of inner errors

for i in range(31):
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
print(numberofInnerErrors)
n = plt.bar(x, numberofInnerErrors)
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


if __name__ == "__main__":
    test = getDiffrencesIndex(['12', '12', '12', '12', '12', '13'], [
                              '12', '14', '13', '12', '12', '13'])
    print(test)
