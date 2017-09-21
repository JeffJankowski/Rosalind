def fasta_to_dict(path):
    d = {}
    with open(path) as f:
        for chunk in filter(None, f.read().split('>')):
            lines = chunk.split()
            d[lines[0]] = ''.join(lines[1:])
    return d
