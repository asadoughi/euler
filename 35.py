
def rotate(n):
    n = str(n)
    n = n[-1] + n[:-1]
    return int(n)

def is_circular(prime, primes):
    p = rotate(prime)
    while p != prime:
        if p not in primes:
            return False
        p = rotate(p)
    return True

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
print len(filter(lambda p: is_circular(p, primes), primes))
