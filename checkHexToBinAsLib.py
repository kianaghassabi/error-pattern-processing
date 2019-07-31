from hextobin import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol
from hextobin import RemoveDifferentSize,TotalBitFlipPerGeneration,ErrorIndices,readFromFile,TotalBitFlipPerGenerationforbits,ErrorIndicesforbits
from hextobin import Plot
import matplotlib.pyplot as plt


sentPacket = [['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']]

recivedPack = [['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
              ,
              ['51', '65', '2E', '64', '39', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']
              ,
             ['52', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '15']
              ]

#BYTE FUNCTIONS
#change all the receivedpack with read from file
#convert the sent packet into bits e.g. '53'='0', '1', '0', '1', '0', '0', '1', '1'

#read received packets from file
readfile=readFromFile("ReceivedPackets1.txt")

#remove the packets with  diffrent lengthes
ErrorPatternsinHexByte=RemoveDifferentSize(recivedPack,31)
print("------BYTE-------")


#THIS FUNCTION WORKS WELL
#Errors per symbol 
IndiciesOfError=ErrorIndices(sentPacket,ErrorPatternsinHexByte) 
#print(indiciedoferror) will give :  [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 27, 28, 29, 30]]
print("IndiciesOfError - byte: ",IndiciesOfError)

#THIS FUNCTION WORKS WELL
#number of Inner Errors in each symbol per generetion
NumberofInnerErrors=TotalBitFlipPerGeneration(sentPacket,ErrorPatternsinHexByte)
print('NumberofInnerErrors - byte: ',NumberofInnerErrors)
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
print("IndiciesOfError - bit",IndiciesOfError)


# THIS FUNCTION WORKS WELL
# #number of Inner Errors in each symbol per generetion
NumberofInnerErrors=TotalBitFlipPerGenerationforbits(sentPacketInBits,errorPatternSplitedBit)
print('NumberofInnerErrors - bit',NumberofInnerErrors)
#print(NumberofInnerErrors) will give :  [6, 9]



Plot(248,IndiciesOfError,"Error indicies in bits","#Inner errors","Packet Percentage",0,248,0,45)
