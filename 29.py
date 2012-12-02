

Q = set()

for i in range(2, 101):
    for j in range(2, 101):
        Q.add(i**j)

print len(Q)
