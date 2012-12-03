
def pandify(a, n):
    ret = ''
    for i in range(1,n+1):
        ret += str(a * i)
    return ret

def is_panda(s):
    if len(s) != 9: return False
    all = set(map(str, range(1,10)))
    for char in s:
        all.discard(char)
    return len(all) == 0

largest = 0
for a in range(10000):
    for b in range(1,10):
        n = pandify(a,b)
        if is_panda(n):
            n = int(n)
            if n > largest:
                largest = n
print largest
