
largest = 0
for a in range(1, 100):
    for b in range(1, 100):
        v = a ** b
        v = str(v)
        # so lazy..
        x = sum(map(int, v))
        if x > largest:
            largest = x
print largest
