

def sieve_of_eratosthenes(max_value):
    primes = range(2, max_value + 1)
    i = 0
    while i < len(primes):
        for j in range(i + primes[i], len(primes), primes[i]):
            primes[j] = 0
        i += 1
        while i < len(primes) and primes[i] == 0:
            i += 1
    primes = filter(lambda x: x != 0, primes)
    return primes

primes = set(sieve_of_eratosthenes(1000000))
max_primes = 0
max_a = None
max_b = None
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        f = lambda n: n*n + a*n + b
        y = f(n)
        while y in primes:
            n += 1
            y = f(n)
        if n > max_primes:
            max_primes = n
            max_a = a
            max_b = b

print max_a * max_b

