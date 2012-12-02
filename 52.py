
def sd(o,x):
    o = str(o)
    x = str(x)
    for digit in x:
        if digit not in o:
            return False
    for digit in o:
        if digit not in x:
            return False
    return True

def test(x):
    a = x + x
    b = a + x
    c = b + x
    d = c + x
    e = d + x
    return sd(a,x) and sd(b,x) and sd(c,x) and sd(d,x) and sd(e,x)

x = 0
while True:
    x += 1
    if test(x):
        print x
        break
