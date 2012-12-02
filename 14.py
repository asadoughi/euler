#!/usr/bin/env python

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
def chain(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return 1 + chain(n >> 1)
    else:
        return 1 + chain(3*n + 1)

longest_chain = None
longest_chain_size = 0
for i in xrange(1, 1000000):
    if chain(i) > longest_chain_size:
        longest_chain_size = chain(i)
        longest_chain = i

print longest_chain, longest_chain_size
    
