from HextoBinLib import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol
from HextoBinLib import RemoveDifferentSize,TotalBitFlipPerGeneration,ErrorIndices,readFromFile,ErrorIndicesforbits 
import matplotlib.pyplot as plt
from PlotterLib import plotBitErrorDistributionOverAllErrorPatterns,plotBitErrorDistributionOverAllErrorPatternsByPercentage,plotBurstErrorCalculatorForBit,plotAvgBitErrorPerSymbol
from PlotterLib import plotBitErrorNumberForEachGeneration,errorCorrectionNumberForDifferentMDSCodes,errorCorrectionPercentageForDifferentMDSCodes

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
    recivedPack=readFromFile("ReceivedPackets1.txt")
    # print("total received packets: ")
    # print(len(recivedPack))
    print(" ------ ")
    ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
    print("fucntion for byte called above")


    #remove the packets with  diffrent lengthes
    print("------BYTE-------")

    #THIS FUNCTION WORKS WELL
    #Errors per symbol 
    # IndiciesOfError=ErrorIndices(sentPacket,ErrorPatternsinHexByte) 

    #THIS FUNCTION WORKS WELL
    #number of Inner Errors in each symbol per generetion
    # NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacket,ErrorPatternsinHexByte)

    #plotter for bytes
    # # 1
    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError)
    # #2
    # plotBitErrorNumberForEachGeneration(IndiciesOfError)
    # #3
    # plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError)
    # #4
    # plotBurstErrorCalculatorForBit(IndiciesOfError)
    # #5
    # plotAvgBitErrorPerSymbol(IndiciesOfError,len(ErrorPatternsinHexByte))
    

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

    NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacketInBits,errorPatternSplitedBit)

    # errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError)
    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError)

    #plotter for bytes
    #1
    # plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError)
    #2
    # plotBitErrorNumberForEachGeneration(IndiciesOfError)
    #3
    # plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError)
    #4
    # plotBurstErrorCalculatorForBit(IndiciesOfError)
    #5
    # plotAvgBitErrorPerSymbol(IndiciesOfError,len(ErrorPatternsinHexByte))
<<<<<<< HEAD
    #6
    # errorCorrectionPercentageForDifferentMDSCodes(IndiciesOfError)
    #7
    errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError)
=======
>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a

    print("End")