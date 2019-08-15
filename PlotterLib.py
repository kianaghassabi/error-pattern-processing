from HextoBinLib import countTheErrorAverageForEachSymbol, innerErrorDistributionCounterForBit 
from HextoBinLib import innerErrorDistributionPercentageForBit , burstErrorCalculatorForBit
import matplotlib.pyplot as plt

def plotter(numberOfBits, resultList, PlotTitle, plotXLabel, pltYLabel, XrangeFrom, XrangeTo, YrangeFrom, YrangeTo):
    # initilizing
    # mu = InputMu
    # sigma = InputSimga
    x = []
    for i in range(numberOfBits):
        x.append(i)

    # innerErrorDistributionPercentage
    # print(innerErrorDistributionPercentage(ListofInnerErrors)) what is it ?
    plt.bar(x, resultList)
    plt.title(PlotTitle)
    plt.xlabel(plotXLabel)
    plt.ylabel(pltYLabel)

    plt.axis([XrangeFrom, XrangeTo, YrangeFrom, YrangeTo])
    plt.grid(True)
    plt.show()
# function  1
def plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError):
    '''
    Receives a list of bit error indicies and plots
    the number of errors in each index ( Bit indicies ) over all given error patterns
    '''
    answer = innerErrorDistributionCounterForBit(IndiciesOfError)
    print(answer)
    plotter(248,answer,"Number of bit errors (Y axis) for each index ( X axis) ","Indicies","# Bit errors",0,248,0,650)

# function  3
def plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError):
    '''
    Receives a list of bit error indicies and plots the percentage of error (Y axis) in each index (X axis)
    over all error patterns for instance, 30% of all first bits over all-error-patterns are errors
    '''
    answer = innerErrorDistributionPercentageForBit(IndiciesOfError)
<<<<<<< HEAD
    plotter(248,answer,"Percentage of bit errors indicies distribution over all packets","indicies","%Error",0,248,0,0.1)
# function  4
=======
    plotter(248,answer,"Percentage of bit errors indicies distribution over all packets","indicies","%Error",0,248,0,0.2)

>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a
def plotBurstErrorCalculatorForBit(IndiciesOfError):
    '''
    Receives a list of bit error indicies and plots the number of burst bit errors (Y axis) by 
    their length (X axis) over all-error-patterns
    '''
    answer = burstErrorCalculatorForBit(IndiciesOfError)
<<<<<<< HEAD
    plotter(248,answer,"Total number of burst errors over all error patterns","Burst error lenght","#Count",0,10,0,30000)

# function  5
=======
    plotter(248,answer,"Total number of burst errors over all error patterns","Burst error lenght","#Count",0,30,0,15000)

>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a
def plotAvgBitErrorPerSymbol(IndiciesOfError,totalErrorPattern):
    '''
    Receives a list of bit error indicies and for each symbol plots the average number of errors
    over all received error patterns
    '''
    errorCountPerIndicies = innerErrorDistributionCounterForBit(IndiciesOfError)
    
    answer = countTheErrorAverageForEachSymbol(errorCountPerIndicies,totalErrorPattern)
    # pass it to another function to return an array 248/8 show the avg error
    # print(len(answer))
<<<<<<< HEAD
    plotter(len(answer),answer,"Average number of bir errors (Y axis) within a symbol  for all symbols ( X axis ) over all packet","symbol index","avg number of bit error",0,len(answer),0,0.5)

# function  2
=======
    plotter(len(answer),answer,"Average number of bir errors (Y axis) within a symbol  for all symbols ( X axis ) over all packet","symbol index","avg number of bit error",0,len(answer),0,0.7)

>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a
def plotBitErrorNumberForEachGeneration(IndiciesOfError):
    '''
    receives a list of bit error indicies over all generations and **calculates**
    the average number of bit errors for all received error patterns
    moreover, plots the number of bit errors within a received error patterns ( Y axis )
    for each received packet (X axis)
    '''

    #  ***  it is better to put all computational steps into another function 
    #  *** like other functions 
    NumberOfBitErrorForEachGeneration = []
    sum = 0 
    for InnerListOfErrorIndicies in IndiciesOfError:
        NumberOfBitErrorForEachGeneration.append(len(InnerListOfErrorIndicies))
        sum +=len(InnerListOfErrorIndicies)

    answer = NumberOfBitErrorForEachGeneration
    print("The average is ", float(sum)/float(len(NumberOfBitErrorForEachGeneration)))
<<<<<<< HEAD
    plotter(len(answer),answer,"Number of bit errors within a received error pattern (generation) ","Received Packet Index","# Bit errors",0,len(answer),0,50)
    
# function  6
=======
    plotter(len(answer),answer,"Number of bit errors within a received error pattern (generation) ","Received Packet Index","# Bit errors",0,len(answer),0,30)
    
>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a
def errorCorrectionPercentageForDifferentMDSCodes(IndiciesOfError):
    '''
    receives a list of bit error indicies over all received error patterns and returns  the percentage of packets
    that could be corrected ( Y axis ) with an MDS code 
    with different errorCorrectionCapabilities ( X axis )
    '''
    #  Actually I'm trying to say " Age MDS code ba felan Error capabilitie estefade konim felan darsad az 
    #  error haro dorost konim"  :-D


    #  ***  it is better to put all computational steps into another function 
    #  *** like other functions 


    numberOfErrorDistributionOverAllReceivedPacket = [ 0 for i in range(8*31)]
    for InnerListOfErrorIndicies in IndiciesOfError:
        numberOfErrorDistributionOverAllReceivedPacket[len(InnerListOfErrorIndicies)] +=1

    CDF = [ 0 for i in range(8*31)]

    CDF[0] = numberOfErrorDistributionOverAllReceivedPacket[0]
    for i in range(1,len(numberOfErrorDistributionOverAllReceivedPacket)):
        CDF[i] = CDF[i-1] + numberOfErrorDistributionOverAllReceivedPacket[i] 

    # percentage
    for i in range(len(CDF)):
        CDF[i] = (CDF[i] / len(IndiciesOfError))*100
    print(numberOfErrorDistributionOverAllReceivedPacket)
    answer = CDF
<<<<<<< HEAD
    plotter(len(answer),answer,"=% of the corrected packets with the different MDS error correction rates ","MDS error correction","%Correction",0,250,0,100)

# function  7
=======
    plotter(len(answer),answer,"=% of the corrected packets with the different MDS error correction rates ","MDS error correction","%Correction",0,50,0,100)

>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a
def errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError):
    '''
    receives a list of bit error indicies over all received error patterns and returns  the number of packets
    that could be corrected ( Y axis ) with an MDS code 
    with different errorCorrectionCapabilities ( X axis )
    '''
    #  Actually I'm trying to say " Age MDS code ba felan Error capabilitie estefade konim felan tedad az 
    #  error haro dorost konim"  :-D

    #  ***  it is better to put all computational steps into another function 
    #  *** like other functions 

    numberOfErrorDistributionOverAllReceivedPacket = [ 0 for i in range(8*31)]
    for InnerListOfErrorIndicies in IndiciesOfError:
        numberOfErrorDistributionOverAllReceivedPacket[len(InnerListOfErrorIndicies)] +=1

    CDF = [ 0 for i in range(8*31)]

    CDF[0] = numberOfErrorDistributionOverAllReceivedPacket[0]
    for i in range(1,len(numberOfErrorDistributionOverAllReceivedPacket)):
        CDF[i] = CDF[i-1] + numberOfErrorDistributionOverAllReceivedPacket[i] 


    print(numberOfErrorDistributionOverAllReceivedPacket)
    answer = CDF
<<<<<<< HEAD
    plotter(len(answer),answer,"# of the corrected packets with the different MDS error correction rates","MDS error correction rate","#Correction",0,250,0,14000)
=======
    plotter(len(answer),answer,"# of the corrected packets with the different MDS error correction rates","MDS error correction rate","#Correction",0,50,0,6100)
>>>>>>> 89cc528d9f5bef81f357035be1aa025db5bfbd7a

    