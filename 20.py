
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

fac_100 = fac(100)
total = 0
while fac_100 > 0:
    total += fac_100 % 10
    fac_100 /= 10
print total
