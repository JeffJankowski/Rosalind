rna_codon = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
             'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
             'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
             'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
             'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
             'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
             'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
             'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
             'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
             'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
             'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
             'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
             'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
             'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
             'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
             'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

def split(s, n):
    return [s[start:start+n] for start in range(0, len(s), n)]

def protein_encode(rna):
    encoded = []
    for chunk in split(rna, 3):
        val = rna_codon[chunk]
        if val == 'Stop':
            break
        else:
            encoded.append(val)
    return ''.join(encoded)


with open('data/rosalind_prot.txt') as f:
    print(protein_encode(f.read().strip()))
