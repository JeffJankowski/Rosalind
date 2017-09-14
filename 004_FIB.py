def rabbits(n, k):
    comp = [1, 1]
    for i in range(2, n):
        comp.append(comp[i-2] * k + comp[i-1])
    return comp[n-1]

months, litter = [int(x) for x in open('data/rosalind_fib.txt', 'r').read().strip().split(' ')]
print(rabbits(months, litter))