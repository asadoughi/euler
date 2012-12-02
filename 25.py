#!/usr/bin/env python

from functools import wraps
from math import log, floor

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
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def num_digits(n):
    return floor(round(log(n, 10),1)) + 1

n = 0
while True:
    if num_digits(fib(n)) == 1000:
        print n
        break
    n += 1
