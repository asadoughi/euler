
from collections import defaultdict

f = open('keylog.txt')
nums = map(int, f.readlines())

before = defaultdict(set)
after = defaultdict(set)
map(lambda i: after[i], range(10))
for j in nums:
    l,m,r = j / 100, (j%100)/10, j%10
    before[m].add(l)
    before[r].add(l)
    before[r].add(m)
    after[l].add(m)
    after[l].add(r)
    after[m].add(r)

for i in range(10):
    print i, before[i], after[i]
