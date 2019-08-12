#a list containing all errors
AllErrors=[]

#open File
receivedPacketFile=open("ReceivedPackets1.txt","r")
while True:
    #get line by line
    readline=receivedPacketFile.readline()
    readline=readline.strip()
    line=readline.split(' ')
    if not readline:
        break
    #temp list for each line
    AllErrors.append(line)
    
    #addding to the list of all errors so we would have a list conting other lists

receivedPacketFile.close()


b=[]
b.append([0,1,7,7])
b.append([1,1,2,3])
b.append([7,23])

def count_elements(seq):
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        for j in i:
            hist[j] = hist.get(j, 0) + 1
    return hist


counted = count_elements(b)

print(counted)
