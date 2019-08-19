from HextoBinLib import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol
from HextoBinLib import RemoveDifferentSize,TotalFlipPerGeneration,ErrorIndicesForSymbols,readFromFile,ErrorIndicesforbits 
import matplotlib.pyplot as plt
from PlotterLib import plotBitErrorDistributionOverAllErrorPatterns,plotErrorDistributionOverAllErrorPatternsByPercentage,plotBurstError,plotAvgBitErrorPerSymbol
from PlotterLib import plotErrorNumberForEachGeneration,errorCorrectionNumberForDifferentMDSCodes,errorCorrectionPercentageForDifferentMDSCodes
from math import floor
def averageBitAndSymbolErrorsForDB(listOfNumberOfSymbolErrors,listOfNumberOfBitErrors):

    avgSymbolErrors = 0 
    avgBitErrors = 0
    for tempError in listOfNumberOfSymbolErrors:
        avgSymbolErrors +=tempError

    for tempError in listOfNumberOfBitErrors:
        avgBitErrors +=tempError
    
    print ("Average symbol Errors per packet: ", avgSymbolErrors / len(listOfNumberOfSymbolErrors))
    print ("Average bit Errors per packet: ", avgBitErrors / len(listOfNumberOfBitErrors))

    return
    

def countTheNumberOfBitErrorInEachSymbol(indicesOferrors):
    '''
    receives lists of bit error locations (indices) and returns list of 
    number of bit error within each packet
    '''
    # 31 : number of symbol in each generation
    answer = [ [ 0 for j in range (31)]  for i in range(len(indicesOferrors))]
 
    for i in range (len(indicesOferrors)):
        for j in range (len(indicesOferrors[i])):
            answer[i][floor(indicesOferrors[i][j]/8)] +=1
    return answer


def avgBitErrorWithinDamagedSymbols(indicesOferrors):
    '''
    receives lists of bit error locations (indices) and returns 
    the average number of bit errors in damaged symbols
    '''
    listOfBitErrorWithinSymbols = countTheNumberOfBitErrorInEachSymbol(indicesOferrors)

    damagedSymbolCounter = 0 
    totalBitErrorsInDamagedSymbols = 0 ; 

    for i in range (len(listOfBitErrorWithinSymbols)):
        for j in range(len(listOfBitErrorWithinSymbols[i])):
            if(listOfBitErrorWithinSymbols[i][j]!=0):
                damagedSymbolCounter +=1
                totalBitErrorsInDamagedSymbols +=listOfBitErrorWithinSymbols[i][j]

    print("Damaged Symbols Over all packets --> ", damagedSymbolCounter )
    print("Total bit errors in damaged symbols over all packets --> ", totalBitErrorsInDamagedSymbols )
    print("Average bit error over all damaged symbols --> ", float(totalBitErrorsInDamagedSymbols )/float(damagedSymbolCounter))





if __name__ == "__main__":

    sentPacket = [['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
                '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']]

    # recivedPack = [['50', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
    #             '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
    #             ,
    #             ['50', '65', '2E', '64', '39', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
    #             '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
    #             ,
    #             ['50', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
    #             '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '15']
    #             ]

    #BYTE FUNCTIONS
    #change all the receivedpack with read from file
    #convert the sent packet into bits e.g. '53'='0', '1', '0', '1', '0', '0', '1', '1'

    #read received packets from file
    recivedPack=readFromFile("ReceivedPackets4.txt")
    # print("total received packets: ")
    # print(len(recivedPack))
    print(" ------ ")
    ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
    print("fucntion for byte called above")


    #remove the packets with  diffrent lengthes
    print("------BYTE(symbol)-------")

    #THIS FUNCTION WORKS WELL
    #Errors per symbol 
    IndiciesOfError=ErrorIndicesForSymbols(sentPacket,ErrorPatternsinHexByte) 

    #THIS FUNCTION WORKS WELL
    #number of symbol error per generetion
    numberofSymbolErrorsPerPacket=TotalFlipPerGeneration(sentPacket,ErrorPatternsinHexByte)


    #plotter for bytes/Symbols
    # # 1
    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError ,"symbol")
    # #2
    # plotErrorNumberForEachGeneration(IndiciesOfError ,"symbol")
    # #3
    # plotErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError ,"symbol")
    # #4
    # plotBurstError(IndiciesOfError ,"symbol")
    # #5
    # errorCorrectionPercentageForDifferentMDSCodes(IndiciesOfError,"symbol")
    # #6
    # errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError,"symbol")
    
    

    #########################################PER BITS##################################################
    print("------BIT-------")
    sentPacketInBits=IntoBitGeneration(sentPacket)

    ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
    print("fucntion for byte differences called above")

    ErrorPatternsinBinBit=IntoBitGeneration(ErrorPatternsinHexByte)

    #248 = 31*8
    errorPatternSplitedBit=RemoveDifferentSize(ErrorPatternsinBinBit,248)
    print("fucntion for bit differences called above")


    IndiciesOfError=ErrorIndicesforbits(sentPacketInBits,errorPatternSplitedBit) 

    numberOfBitErrorsPerPacket=TotalFlipPerGeneration(sentPacketInBits,errorPatternSplitedBit)

    

    #plotter for bits
    #1
    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError ,"bit")
    #2
    # plotErrorNumberForEachGeneration(IndiciesOfError,"bit")
    #3
    # plotErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError,"bit")
    #4
    # plotBurstError(IndiciesOfError,"bit")
    #5 
    # plotAvgBitErrorPerSymbol(IndiciesOfError,len(ErrorPatternsinHexByte),"bit")
    #5
    # errorCorrectionPercentageForDifferentMDSCodes(IndiciesOfError,"bit")
    #6
    # errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError,"bit")

    #new ****
    # (Nazari) : Kiana jan ino lotfan move kon to lib mortabetesh
    


    #Average Bit and Symbol Error
    # averageBitAndSymbolErrorsForDB(numberofSymbolErrorsPerPacket,numberOfBitErrorsPerPacket)
    avgBitErrorWithinDamagedSymbols(IndiciesOfError)

    print("End")