import urllib.request
import re

def get_fasta(id):
    data = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{id}.fasta').read()
    return ''.join(data.decode('utf-8').splitlines()[1:])

# found a this trick on SO; group the pattern and we can find overlapping matches
__compiled__ = re.compile(r'(?=(N[^P][ST][^P]))')
def contains_N_glyc(fasta):
    return [match.span()[0]+1 for match in __compiled__.finditer(fasta)]


with open('data/rosalind_mprt.txt') as f:
    ids = f.read().strip().split()
    for id in ids:
        positions = contains_N_glyc(get_fasta(id))
        if positions:
            print(id)
            print(*positions)