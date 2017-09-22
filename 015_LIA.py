from math import factorial

def choose(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

def prob(k, N):
    total = 0
    pop = 2**k
    for i in range(N, pop + 1):
        total += choose(pop, i) * 0.25**i * 0.75**(pop-i)
    return total


with open('data/rosalind_lia.txt') as f:
    k, N = [int(x) for x in f.readline().split(' ')]
    print(round(prob(k, N), 3))