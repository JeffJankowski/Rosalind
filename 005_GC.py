def gc_content(dna):
    return ((dna.count('C') + dna.count('G')) / len(dna)) * 100.0

def fasta_to_dict(path):
    d = {}
    with open(path) as f:
        for chunk in filter(None, f.read().split('>')):
            lines = chunk.split()
            d[lines[0]] = ''.join(lines[1:])
    return d


dna_map = fasta_to_dict('data/rosalind_gc.txt')
gc_map = {k: gc_content(dna_map[k]) for k in dna_map.keys()}
max_gc_key = max(gc_map.keys(), key=gc_map.get)
print('%s\n%.6f' % (max_gc_key, gc_map[max_gc_key]))
