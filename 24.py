
def y(x):
    if len(x) == 1:
        return [x[0]]
    result = []
    for i in range(len(x)):
        for j in y(x[:i] + x[i+1:]):
            result += [x[i] + j]
    return result
           
x = map(str, range(10))     
x.pop(2)
result = y(x)
i = 999999 - 2*362880
print '2' + result[i]


    
