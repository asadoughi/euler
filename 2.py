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
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = 1
sum = 0
while fib(n) <= 4000000:
    if fib(n) % 2 == 0:
        sum += fib(n)
    n += 1
print sum
