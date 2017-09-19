def prob_dominant(k, m, n):
    t = k + m + n
    # P(homog_dom) + P(hetero) + P(homog_recess)
    return (1/t * k) + \
           (1/t * k/(t-1) + 1/t * (m-1)/(t-1) * 0.75 + 1/t * n/(t-1) * 0.5) * m + \
           (1/t * k/(t-1) + 1/t * m/(t-1) * 0.5) * n


k, m, n = [int(x) for x in open('data/rosalind_iprb.txt', 'r').read().strip().split(' ')]
print(f'{prob_dominant(k, m, n):.6f}')