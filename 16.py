
def rca(a, b, base = 10):
    i = 0
    sum = []
    carry = 0
    while i < len(b) or i < len(a):
        a_i = 0
        b_i = 0
        if i < len(a):
            a_i = a[i]
        if i < len(b):
            b_i = b[i]
        total = a_i + b_i + carry
        carry = total / base
        sum.append(total % base)
        i += 1

    if carry > 0:
        sum.append(carry)
        
    return sum

a = [1]
for i in range(1001):
    print i, reduce(lambda x,y: x+y, a)
    a = rca(a, a)
