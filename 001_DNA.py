# returns a tuple of the counts in the order: A, C, G, T
def count_nucleotides(dna):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in dna:
        count[c.upper()] += 1
    return count['A'], count['C'], count['G'], count['T']

data = open('data/rosalind_dna.txt', 'r').read()
A, C, G, T = count_nucleotides(data)
print(A, C, G, T)