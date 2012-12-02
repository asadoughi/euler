
def d(n):
    return sum([i for i in range(1, n) if n%i == 0])

total = 0
for i in range(1, 10000):
    result = d(i)
    if i != result and d(result) == i:
        total += i
print total
