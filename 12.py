
from collections import defaultdict

# sources: http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number http://mathforum.org/library/drmath/view/55843.html

# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2

# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = defaultdict(int)
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] += 1
    if n == 1:
      return d

def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  mul = lambda x,y: x*y
  return reduce(mul, powers_plus, 1)

def triangle(n):
  return n*(n+1) >> 1

i = 1
while True:
  nd = NumberOfDivisors(triangle(i)) 
  if nd > 500:
    print i, triangle(i), nd
    exit()
  i += 1
