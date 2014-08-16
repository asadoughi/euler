squares = [2 * i * i for i in range(1, 100)]

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
    
primes = sieve_of_eratosthenes(10000)
primes = set([p for p in primes if p != 0])


for i in range(33, 10000, 2):
    if i in primes:
        continue
    solved = False
    for s in squares:
        if s > i:
            break
        if (i - s) in primes:
            solved = True
    if not solved:
        print i
        break
