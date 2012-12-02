#!/usr/bin/env python

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
    
num = 600851475143
primes = sieve_of_eratosthenes(10000000)
primes = filter(lambda x: x != 0, primes)
primes.reverse()

for prime in primes:
    if num % prime == 0:
        print prime
        break
