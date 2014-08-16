def sieve_of_eratosthenes(max_value):
    prime_nums = range(2, max_value + 1)
    i = 0
    while i < len(prime_nums):
        for j in range(i + prime_nums[i], len(prime_nums), prime_nums[i]):
            prime_nums[j] = 0
        i += 1
        while i < len(prime_nums) and prime_nums[i] == 0:
            i += 1
    return prime_nums
    
primes = sieve_of_eratosthenes(1000000)
primes = [p for p in primes if p != 0]


def memoize(f):
    cache = dict()
    def wrapped_f(i):
        if not cache.get(i):
            cache[i] = f(i)
        return cache[i]
    return wrapped_f

@memoize
def factor(i):
    if i == 1:
        return set()
    for p in primes:
        if i % p == 0:
            return set([p]) | factor(i / p)

lim = 4
for n in range(2, 1000000):
    g = factor(n)
    h = factor(n+1)
    i = factor(n+2)
    j = factor(n+3)
    if (len(g) >= lim and len(h) >= lim and len(i) >= lim and len(j) >= lim
        and len(g | h | i | j) > lim):
        print n, n+1, n+2, n+3
        print g, h, i, j
        break
