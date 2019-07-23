

# a = [0, 1, 1, 1, 2, 3, 7, 7, 23]
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



#ye araye dashte basham k index error haro dashte bashe