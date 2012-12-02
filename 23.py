
def divisors(n):
    return [i for i in range(1,n/2 + 1) if n % i == 0]

abundants = set()
for i in range(12, 28124):
    if sum(divisors(i)) > i:
        abundants.add(i)

s = sorted(abundants)
total = 0
for i in range(1,28124):
    for a in s:
        if a > i:
            break
        b = i - a
        if b in abundants:
            total += i
            break

print 28123*28124/2 - total
        
