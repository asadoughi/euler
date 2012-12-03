
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

primes = sieve_of_eratosthenes(9999)
primes = filter(lambda p: p > 1000, primes)
sprimes = set(primes)

def permute(n):
    if len(n) == 0:
        return []

    ret = []
    for i in range(len(n)):
        r = permute(n[:i] + n[i+1:])
        if len(r) == 0:
            ret += [n[i]]
        else:
            for x in r:
                ret += [n[i] + x]
    return ret

sets = []
done = {}
for p in primes:
    l = set()
    if p in done: continue

    for perm in map(int, permute(str(p))):
        if perm in sprimes:
            l.add(perm)
    
    for x in l:
        done[x] = 1

    if len(l) >= 3:
        sets.append(l)

def choose3(s):
    ret = set()
    for x in s:
        for y in s:
            if x >= y: continue
            c = y - x
            d = y + c
            if d in s:
                ret.add((x,y,d))
    return ret

for s in sets:
    y = choose3(s)
    if len(y) > 0:
        print y
