def transcribe(dna):
    return dna.replace('T', 'U')

data = open('data/rosalind_rna.txt', 'r').read().strip()
print(transcribe(data))