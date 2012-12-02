
def sieve_of_eratosthenes(max_value):
    primes = range(2, max_value + 1)
    i = 0
    while i < len(primes):
        for j in range(i + primes[i], len(primes), primes[i]):
            primes[j] = 0
        i += 1
        while i < len(primes) and primes[i] == 0:
            i += 1
    return filter(lambda x: x != 0, primes)

def tr(p):
    p = str(p)
    return map(int, [p[i:] for i in range(1,len(p))] + \
                   [p[:i] for i in range(1,len(p))])

primes = set(sieve_of_eratosthenes(1000000))
tprimes = set()
for p in primes:
    truncatable = True
    if p <= 7: continue
    for x in tr(p):
        if x not in primes:
            truncatable = False
            break
    if truncatable:
        tprimes.add(p)
print sum(tprimes)
