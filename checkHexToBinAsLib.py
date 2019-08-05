from hextobin import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol
from hextobin import RemoveDifferentSize,TotalBitFlipPerGeneration,ErrorIndices,readFromFile,ErrorIndicesforbits , countTheErrorAverageForEachSymbol
from hextobin import plotter , innerErrorDistributionCounterForBit, innerErrorDistributionPercentageForBit , burstErrorCalculatorForBit
import matplotlib.pyplot as plt




def plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError):
    '''
    Enter the indicies of error and you'll receive 
    the count errors of each index over all given error patterns
    '''
    answer = innerErrorDistributionCounterForBit(IndiciesOfError)
    print(answer)
    plotter(248,answer,"Bit errors indicies distribution over all packets","indicies","#Errors",0,248,0,400)


def plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError):
    '''
    Enter the indicies of error and it'll calculate
    percentage of errors of each index over all given error patterns
    '''
    answer = innerErrorDistributionPercentageForBit(IndiciesOfError)
    plotter(248,answer,"Percentage of bit errors indicies distribution over all packets","indicies","%Error",0,248,0,1)

def plotBurstErrorCalculatorForBit(list):
    '''
    plots the number of burst errors over all-error-patterns
    '''
    answer = burstErrorCalculatorForBit(list)
    plotter(248,answer,"Total number of burst error over all error patterns","burst lenght","count",0,30,0,15000)

def plotAvgBitErrorPerSymbol(list,totalErrorPattern):
    '''
    For each symbol find the avg of error over all received error pattern
    '''
    errorCountPerIndicies = innerErrorDistributionCounterForBit(list)
    
    answer = countTheErrorAverageForEachSymbol(errorCountPerIndicies,totalErrorPattern)
    # pass it to another function to return an array 248/8 show the avg error
    # print(len(answer))
    plotter(len(answer),answer,"Average error within a symbol over all packet","symbol index","avg number of error",0,len(answer),0,0.7)

def plotBitErrorNumberForEachGeneration(list):
    '''
    receives  lists of  error indicies over all generations and calculates
    the avg number of error ( in bits ) for all received error patterns
    '''
    NumberOfBitErrorForEachGeneration = []
    sum = 0 
    for InnerListOfErrorIndicies in list:
        NumberOfBitErrorForEachGeneration.append(len(InnerListOfErrorIndicies))
        sum +=len(InnerListOfErrorIndicies)

    answer = NumberOfBitErrorForEachGeneration
    print("The average is ", float(sum)/float(len(NumberOfBitErrorForEachGeneration)))
    plotter(len(answer),answer,"Bit Error within a Received error pattern","Received Packet Index","#error",0,len(answer),0,50)
    




if __name__ == "__main__":

    sentPacket = [['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
                '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']]

    recivedPack = [['50', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
                '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
                ,
                ['50', '65', '2E', '64', '39', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
                '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
                ,
                ['50', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
                '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '15']
                ]

    #BYTE FUNCTIONS
    #change all the receivedpack with read from file
    #convert the sent packet into bits e.g. '53'='0', '1', '0', '1', '0', '0', '1', '1'

    #read received packets from file
    recivedPack=readFromFile("ReceivedPackets1.txt")
    ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)

    #remove the packets with  diffrent lengthes
    # ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
    print("------BYTE-------")


    #THIS FUNCTION WORKS WELL
    #Errors per symbol 
    IndiciesOfError=ErrorIndices(sentPacket,ErrorPatternsinHexByte) 
    #print(indiciedoferror) will give :  [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 27, 28, 29, 30]]
    # print("IndiciesOfError - byte: ",IndiciesOfError)

    #THIS FUNCTION WORKS WELL
    #number of Inner Errors in each symbol per generetion
    NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacket,ErrorPatternsinHexByte)
    # print('NumberofInnerErrors - byte: ',NumberofInnerErrors)
    #print(NumberofInnerErrors) will give :  [6, 9]

    print("------BIT-------")
    #########################################PER BITS##################################################

    sentPacketInBits=IntoBitGeneration(sentPacket)
    # print("sentPacketInBits->",sentPacketInBits)
    # print("len(sentPacketInBits)",len(sentPacketInBits)*8)

    #remove the packets with  diffrent lengthes in bits
    ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
    # print("****************************" , ErrorPatternsinHexByte)

    #convert all recieved packets into bits e.g.  '53'='0', '1', '0', '1', '0', '0', '1', '1'
    ErrorPatternsinBinBit=IntoBitGeneration(ErrorPatternsinHexByte)
    # print("ErrorPatternsinBinBit->",ErrorPatternsinBinBit)

    #248 = 31*8
    errorPatternSplitedBit=RemoveDifferentSize(ErrorPatternsinBinBit,248)
    # print('len(errorPatternSplitedBit',len(errorPatternSplitedBit))
                
    # THIS FUNCTION WORKS WELL
    #Errors per symbol 
    IndiciesOfError=ErrorIndicesforbits(sentPacketInBits,errorPatternSplitedBit) 
    #print(indiciedoferror) will give :  [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 27, 28, 29, 30]]
    # print("IndiciesOfError - bit",IndiciesOfError)


    # THIS FUNCTION WORKS WELL
    # #number of Inner Errors in each symbol per generetion
    NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacketInBits,errorPatternSplitedBit)
    # print('NumberofInnerErrors - bit',NumberofInnerErrors)

    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError)
    # plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError)

    # TEST BURST ERROR WITH SAMPLEDATA
    # SAMPLEDATA = [[0,1,2,3,4,10,11,12,13,14],[0,1,2,5,6,7,10,11,12,13,14,15],[1,10,120,122]]
    # print(IndiciesOfError)
    # plotBurstErrorCalculatorForBit(IndiciesOfError)

    # plotAvgBitErrorPerSymbol(IndiciesOfError,len(errorPatternSplitedBit))

    plotBitErrorNumberForEachGeneration(IndiciesOfError)
    print("End")