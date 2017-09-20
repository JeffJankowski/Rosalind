from utility import fasta_to_dict

def count_symbols(dnas):
    counts_by_pos = []
    for i in range(len(dnas[0])):
        counts_by_pos.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    for dna in dnas:
        for i, c in enumerate(dna):
            counts_by_pos[i][c] += 1
    return counts_by_pos

def consensus(counts):
    cons = []
    for pos in counts:
        cons.append(max(pos, key=pos.get))
    return ''.join(cons)

def print_counts(counts):
    for symbol in counts[0].keys():
        print(f'{symbol}:', end='')
        for pos in counts:
            print(f' {pos[symbol]}', end='')
        print('')


dnas = list(fasta_to_dict('data/rosalind_cons.txt').values())
counts = count_symbols(dnas)
consensus_str = consensus(counts)
print(consensus_str)
print_counts(counts)