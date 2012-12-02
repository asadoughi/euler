
T = lambda n: n * (n+1) / 2
P = lambda n: n * (3*n-1) / 2
H = lambda n: n * (2*n-1)

t = [T(n) for n in range(286, 100000)]
p = set([P(n) for n in range(166, 100000)])
h = set([H(n) for n in range(144, 100000)])

for num in t:
    if num in p and num in h:
        print num
        exit()
