
from functools import wraps

def memoize(fn):
    cache = {}
    @wraps(fn)
    def wrap(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrap

@memoize
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

def choose(n, r):
    return fac(n) / (fac(r) * fac(n-r))

count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if choose(n,r) > 1000000:
            count += 1
print count
