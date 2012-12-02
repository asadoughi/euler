
sum_total = 0
for i in range(2,1000000):
    total = 0
    j = i
    while i > 0:
        total += (i%10)**5
        i /= 10
    if total == j:
        sum_total += j

print sum_total
