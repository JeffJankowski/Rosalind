def reverse_complement(dna):
    return dna[::-1].replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

data = open('data/rosalind_revc.txt', 'r').read().strip()
print(reverse_complement(data))