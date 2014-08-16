def sieve_of_eratosthenes(max_value):
    prime_nums = range(2, max_value + 1)
    i = 0
    while i < len(prime_nums):
        for j in range(i + prime_nums[i], len(prime_nums), prime_nums[i]):
            prime_nums[j] = 0
        i += 1
        while i < len(prime_nums) and prime_nums[i] == 0:
            i += 1
    prime_nums = [p for p in prime_nums if p != 0]
    return prime_nums
    
primes = sieve_of_eratosthenes(1000000)
primes_set = set(primes)
solutions = []
for i in range(len(primes)):
    total = primes[i]
    if total > 100000:
        break
    for j in range(i+1, i+21):
        total += primes[j]
    for j in range(i+21, len(primes)):
        total += primes[j]
        if total in primes_set:
            solutions.append((i,j,total))
        elif total > 1e6:
            break
longest_p = None
longest = 0
for i,j,p in solutions:
    if j-i+1 > longest:
        longest = j-i+1
        longest_p = p
print longest, longest_p
