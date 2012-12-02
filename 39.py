

def sides(p):
    l = set()
    for a in range(1,p):
        for b in range(1,p-a):
            c = p - b - a
            if c <= 0: continue

            if a*a + b*b == c*c:
                if a < b: 
                    l.add((a,b,c))
                else:
                    l.add((b,a,c))
    return l

largest = 0
largest_p = None
for p in range(1,1001):
    l = len(sides(p))
    if l > largest:
        largest = l
        largest_p = p
print largest_p
