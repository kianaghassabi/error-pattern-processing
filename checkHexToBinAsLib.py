from hextobin import convertErrorPatternIntoBitGeneration as IntoBitGeneration , convertErrorPatternIntoBitSymbol as IntoBitSymbol

h  = ['53', '65', '6E', '64', '69', '6E', '67', '20', '4D', '65', '73', '73', '61', '67',
              '65', '20', '49', '73', '20', '57', '6F', '72', '6B', '69', '6E', '67', '20', '46', '69', '6E', '65']

hPrime = []
hPrime.append(h)
hPrime.append(h)
hPrime.append(h)

answerOne  = IntoBitGeneration(hPrime)
answerTwo = IntoBitSymbol(hPrime)

print ("Stop")
