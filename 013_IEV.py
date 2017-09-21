# 1. AA-AA  100%
# 2. AA-Aa  100%
# 3. AA-aa  100%
# 4. Aa-Aa  75%
# 5. Aa-aa  50%
# 6. aa-aa  0%


def dominant_count(pop):
    return (sum(pop[:3]) + pop[3]*0.75 + pop[4]*0.5)*2


with open('data/rosalind_iev.txt') as f:
    data = [int(x) for x in f.readline().split(' ')]
    print(dominant_count(data))