from utility import fasta_to_dict

def generate_adjacencies(fasta, k=3):
    adj = []
    for id1 in fasta.keys():
        suff = fasta[id1][-k:]
        for id2 in fasta.keys():
            if id1 != id2 and fasta[id2][:k] == suff:
                adj.append((id1, id2))
    return adj


data = fasta_to_dict('data/rosalind_grph.txt')
for source, target in generate_adjacencies(data):
    print(source, target)