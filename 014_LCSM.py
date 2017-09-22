from utility import fasta_to_dict


def longest_substr(dnas):
    min_len_dna = min(dnas, key=lambda x: len(x))
    min_len = len(min_len_dna)
    # start at half length of shortest DNA, because I'm feeling risky
    for size in range(int(min_len/2+.5), 1, -1):
        for i in range(min_len-size+1):
            target = min_len_dna[i:i+size]
            if all((target in dna) for dna in dnas):
                return target


data = fasta_to_dict('data/rosalind_lcsm.txt').values()
print(longest_substr(data))
