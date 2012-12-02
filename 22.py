
f = open("names.txt")
names = [name.strip().replace('"','') for name in f.readline().split(',')]
names = sorted(names)
total = 0
for i in range(len(names)):
    name = names[i]
    score = sum(map(lambda c: ord(c) - ord('A') + 1, name))
    total += (i+1) * score
print total
