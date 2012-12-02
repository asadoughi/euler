
fac = {
    0:1,
    1:1,
    2:2,
    3:6, 
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880,
    }

sum_total = 0
for i in range(3, 1000000):
    j = i
    total = 0
    while i > 0:
        d = fac[i % 10]
        total += d 
        i /= 10

    if total == j:
        sum_total += total

print sum_total
