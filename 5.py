#!/usr/bin/env python

primes = [2,3,5,7,11,13,17,19]
primed = reduce(lambda x,y: x*y, primes)
j = 1
while True:
    num = j * primed
    for i in range(2,21):
        if num % i == 0:
            if i == 20:
                print num
                exit()
        else:
            break
    j += 1
