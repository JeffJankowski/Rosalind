def hamming(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

with open('data/rosalind_hamm.txt') as f:
    dnas = f.readlines()
    print(hamming(dnas[0], dnas[1]))