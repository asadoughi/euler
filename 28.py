
import math

def f(n):
    total = 1
    level_up = 2
    i = 1
    levels = int(math.ceil(n/2))
    for level in range(levels):
        for k in range(4):
            i += level_up
            total += i
        level_up += 2
    return total

print 1, f(1)
print 3, f(3)
print 5, f(5)
print 1001, f(1001)
