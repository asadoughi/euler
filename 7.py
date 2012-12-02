#!/usr/bin/env python

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
    
primes = sieve_of_eratosthenes(10000000)
print primes[10000]
