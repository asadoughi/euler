
l = []
for i in range(10, 100):
    for j in range(10, 100):
        if i >= j: continue

        v = float(i)/j
        si = str(i)
        sj = str(j)
        a, b = si[0], si[1]
        c, d = sj[0], sj[1]
        if a == c and a != '0' and d != '0':
            x = float(b)/float(d)
            if x == v:
                l.append((i,j))
        elif a == d and a != '0' and c != '0':
            x = float(b)/float(c)
            if x == v:
                l.append((i,j))
        elif b == c and b != '0' and d != '0':
            x = float(a)/float(d)
            if x == v:
                l.append((i,j))
        elif b == d and b != '0' and c != '0':
            x = float(a)/float(c)
            if x == v:
                l.append((i,j))

num = 1
den = 1
for m,n in l:
    print m,n
    num *= m
    den *= n
print num, den
