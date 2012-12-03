
def is_panda(s, n):
    all = set(map(str, range(1,n+1)))
    for char in s:
        all.discard(char)
    return len(all) == 0

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

primes = sieve_of_eratosthenes(10000000)
primes.reverse()
for p in primes:
    q = str(p)
    if is_panda(q, len(q)):
        print p
        break
