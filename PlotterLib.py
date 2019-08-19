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
def plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError, mode):
    '''
    Receives a list of bit/symbol error indicies and plots
    the number of errors in each index ( Bit/symbol indicies ) over all given error patterns
    '''
    answer = innerErrorDistributionCounterForBit(IndiciesOfError)
    print(answer)

    if(mode == "symbol"):
        plotter(248,answer,"Total #bit flips (Y axis) within each symbol (X axis) over all packets.","Symbol index","#Bit flips",0,30,0,500)
    else:
        plotter(248,answer,"Total #bit flips (Y axis) for each bit index (X axis) over all packets","Bit index","#Bit flips",0,248,0,150) 


# function  3
#  change percentage to  rate for all functions ****
def plotErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError, mode):
    '''
    Receives a list of bit/symbol error indicies and plots the rate of error (Y axis) in each index (X axis)
    over all error patterns for instance, 30% of all first bits over all-error-patterns are errors
    '''

    # ***  the name of innerErrorDistrubutionPercentageForBit should change to innerErrorDistrubutionPercentage
    answer = innerErrorDistributionPercentageForBit(IndiciesOfError)

    if (mode =="symbol"):
        plotter(248,answer,"Rate of errors for each symbol indicies over all packets","Symbol index"," Error rate",0,30,0,0.2)
    else:
        plotter(248,answer,"Rate of errors for each bit indicies over all packets","Bit index","Error rate",0,248,0,0.08)
    

def plotBurstError(IndiciesOfError, mode):
    '''
    Receives a list of bit/symbol error indicies and plots the number of burst bit errors (Y axis) by 
    their length (X axis) over all-error-patterns
    '''
    answer = burstErrorCalculatorForBit(IndiciesOfError)

    if(mode == "symbol"):
        plotter(248,answer,"Total number of burst symbol errors over all error patterns","Burst errors' lenght","Count",0,31,0,31000)
    else:
        plotter(248,answer,"Total number of burst bit errors over all error patterns","Burst errors' lenght","Count",0,8,0,6000)


   
def plotAvgBitErrorPerSymbol(IndiciesOfError,totalErrorPattern, mode):
    '''
    Receives a list of bit error indicies and for each symbol plots the average number of errors
    over all received error patterns
    '''
    errorCountPerIndicies = innerErrorDistributionCounterForBit(IndiciesOfError)
    
    answer = countTheErrorAverageForEachSymbol(errorCountPerIndicies,totalErrorPattern)
    # pass it to another function to return an array 248/8 show the avg error
    # print(len(answer))
    plotter(len(answer),answer,"Average number of bit errors (Y axis) within each symbol( X axis )","symbol index","Average bit errors",0,len(answer)-1,0,0.3)

# function  2
def plotErrorNumberForEachGeneration(IndiciesOfError, mode):
    '''
    receives a list of bit/symbol error indicies over all generations and **calculates**
    the average number of bit/symbol errors for all received error patterns
    moreover, plots the number of bit/symbol errors within a received error patterns ( Y axis )
    for each received packet (X axis)
    '''

    #  ***  it is better to put all computational steps into another function 
    #  *** like other functions 
    numberOfErrorForEachGeneration = []
    sum = 0 
    for InnerListOfErrorIndicies in IndiciesOfError:
        numberOfErrorForEachGeneration.append(len(InnerListOfErrorIndicies))
        sum +=len(InnerListOfErrorIndicies)

    answer = numberOfErrorForEachGeneration
    print("The average is ", float(sum)/float(len(numberOfErrorForEachGeneration)))

    if(mode == "symbol"):
        plotter(len(answer),answer,"Number of symbol errors within a received error pattern (generation) ","Received Packet Index","#Symbol errors",0,len(answer),0,31)
    else:
        plotter(len(answer),answer,"Number of bit errors within a received error pattern (generation) ","Received Packet Index","#Bit errors",0,len(answer),0,248)



def errorCorrectionPercentageForDifferentMDSCodes(IndiciesOfError, mode):
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

    # because of error correction rate we shouldn't count no bit/symbol errors
    CDF[1] = numberOfErrorDistributionOverAllReceivedPacket[1]

    for i in range(2,len(numberOfErrorDistributionOverAllReceivedPacket)):
        CDF[i] = CDF[i-1] + numberOfErrorDistributionOverAllReceivedPacket[i] 

    correctPacket = numberOfErrorDistributionOverAllReceivedPacket[0]

    # percentage
    for i in range(len(CDF)):
        CDF[i] = (CDF[i] / (len(IndiciesOfError) - correctPacket ))*100

    print(numberOfErrorDistributionOverAllReceivedPacket)
    answer = CDF

    if (mode == "symbol"):
        plotter(len(answer),answer,"%corrected packets with the different MDS symbol correction rates ","MDS symbol error correction capability","%Correction",0,31,0,100)
    else:
        plotter(len(answer),answer,"%corrected packets with the different MDS bit correction rates ","MDS bit error correction capability","%Correction",0,50,0,100)

def errorCorrectionNumberForDifferentMDSCodes(IndiciesOfError, mode):
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
    plotter(len(answer),answer,"# of the corrected packets with the different MDS error correction rates","MDS error correction rate","#Correction",0,250,0,14000)

    