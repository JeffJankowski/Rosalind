def findAll(str, sub):
    idxs = []
    l_sub = len(sub)
    l_str = len(str)
    i = 0
    while i < l_str:
        if str[i:i+l_sub] == sub:
            idxs.append(i)
        i += 1
    return idxs


with open('data/rosalind_subs.txt') as f:
    dna = f.readline()
    substr = f.readline()
    # they want it 1-indexed instead of 0..
    locs = (str(i+1) for i in findAll(dna, substr))
    print(' '.join(locs))