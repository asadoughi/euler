c = (200, 100, 50, 20, 10, 5, 2, 1)

def updated_path(path, i):
    if path is None:
        path = (0,) * len(c)
    return tuple(x + 1 
                 if j == i else x
                 for j, x in enumerate(path))

solution_set = set()
def ways_to_make(y, tab=0, previous_coin=None, path=None):
    if y <= 0:
        return
    for i, coin in enumerate(c):
        if previous_coin is not None:
            if coin > previous_coin:
                continue
        if coin == y:
            # print '%s%s' % ('\t'*tab, coin)
            solution_set.add(updated_path(path, i))
        elif coin < y:
            # print '%s%s' % ('\t'*tab, coin)
            ways_to_make(y - coin, tab + 1, coin, updated_path(path, i))


ways_to_make(200)
print len(solution_set)
