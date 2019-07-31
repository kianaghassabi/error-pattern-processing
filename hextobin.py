import string
# hex2bin

#
h = ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
     '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']

# binvalues=[]
# for i in range(len(h)):
#     binaryValues=bin(int('1'+h[i], 16))[3:]
#     # split it by bits
#     for x in binaryValues:
#         binvalues.append(x)

#  making a list of list
hPrime = []
hPrime.append(h)


# It works
def convertErrorPatternIntoBitGeneration(list):
    ''' Entery is list of all error patterns 
    and return each generation in bit rep
    so the answer will be a 2D list

    [
        [generation one: [first bit of first generation] , [ second bit of first generation], ... so on],
        [generation two: [first bit of second generation] , [ second bit of second generation], ... so on]
    ]

    '''
    errorPatternsInBitRep = []
    counter = 0
    for innerList in list:
        counter += 1
        print(counter)
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
        [ generation one [ symbol one [first bit of first symbol],[],[] ],...],
        [ generation two [ symbol one [first bit of first symbol],[],[] ],...]
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


def singleGenerationToBitRepresentation(list):

    '''
    Change a single generation in Hex form int a single generation into bit representation

    FF AF  ---> 1111 1111  1001 1111
    
    '''

    binvalues = [] 
    innerList = []
    for i in range(len(innerList)):
        binaryValues = bin(int('1'+innerList[i], 16))[3:]
        # split it by bits
    for x in binaryValues:
        binvalues.append(x)


def singleGenerationToSymbolRepresentation(list): 
    '''
    Change the single generation into symbol into bit representation
    FF AF => [
                [ [1] [1] [1] [1] [1] [1] [1] [1]]
                [ [1] [1] [1] [1] [1] [0] [0] [1]]
              ]
    '''
    print("Single Generation")


test = convertErrorPatternIntoBitGeneration(hPrime);

print(test);
