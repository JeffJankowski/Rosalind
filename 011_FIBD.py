def rabbits(life, total):
    comp = [1]*total
    for i in range(2, life + 1):
        comp[i] = comp[i-2] + comp[i-1]
    comp[life] -= 1
    for i in range(life + 1, total):
        comp[i] = comp[i-2] + comp[i-1] - comp[i-life-1]
    return comp[total-1]


n, m = [int(x) for x in open('data/rosalind_fibd.txt', 'r').read().strip().split(' ')]
print(rabbits(m, n))
