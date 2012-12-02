
import operator

string = ''
n = 0
while len(string) < 1000001:
    string += str(n)
    n += 1

print reduce(operator.mul, 
             map(int, [string[10**i] for i in range(7)]))
