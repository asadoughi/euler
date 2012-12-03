
P = lambda n: n * (3*n-1) / 2

p = [P(n) for n in range(1,10000)]
sp = set(p)

smallest_d = float('inf')
for x in p:
    for y in p:
        if x == y: continue
        s = x+y 
        d = y-x
        if s in sp and abs(d) in sp:
            if abs(d) < smallest_d:
                smallest_d = abs(d)
print smallest_d
