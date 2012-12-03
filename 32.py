
def is_panda(s):
    if len(s) != 9: return False
    all = set(map(str, range(1,10)))
    for char in s:
        all.discard(char)
    return len(all) == 0

products = set()
for a in range(1,10000):
    for b in range(1,1000):
        c = a * b
        az = str(a)
        bs = str(b)
        cs = str(c)
        if len(az) + len(bs) + len(cs) == 9:
            if is_panda(az+bs+cs):
                products.add(cs)
print sum(map(int, products))
