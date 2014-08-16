def division(q, d):
    p = 0
    r = 1
    q_to_place = dict()
    while r > 0:
        while q < d:
            p -= 1
            q *= 10
        v = q / d
        if q_to_place.get(q):
            return q_to_place[q] - p
        q_to_place[q] = p
        # print p, q, v
        r = q % d
        q -= v * d

l = [division(1, i) for i in range(2, 1000)]
print max(l)
for i in range(len(l)):
    if max(l) == l[i]:
        print i + 2
        break
