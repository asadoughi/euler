
from collections import defaultdict

def search(triangle):
    dist = defaultdict(int)
    dist[(0,0)] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            up = dist[(i-1,j)]
            up_left = dist[(i-1,j-1)]
            dist[(i,j)] = max([up,up_left]) + triangle[i][j]
                
    return dist
                

f = open('triangle.txt')
triangle = []
for line in f.readlines():
    line = line.strip().split()
    row = []
    for num in line:
        if num[0] == '0':
            num = num[1]
        row.append(int(num))
    triangle.append(row)

distances = search(triangle)
print max(distances.values())

