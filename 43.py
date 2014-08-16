
sum = 0
for d1 in range(1, 10):
    for d2 in range(10):
        if d2 == d1:
            continue
        for d3 in range(10):
            if d3 == d2 or d3 == d1:
                continue
            for d4 in range(0, 10, 2):
                if d4 == d3 or d4 == d2 or d4 == d1:
                    continue
                for d5 in range(10):
                    if d5 == d4 or d5 == d3 or d5 == d2 or d5 == d1:
                        continue
                    if ((d3 * 100 + d4 * 10 + d5) % 3) != 0:
                        continue
                    for d6 in (0, 5):
                        if d6 == d5 or d6 == d4 or d6 == d3 or d6 == d2 or d6 == d1:
                            continue
                        for d7 in range(10):
                            if d7 == d6 or d7 == d5 or d7 == d4 or d7 == d3 or d7 == d2 or d7 == d1:
                                continue
                            if ((d5 * 100 + d6 * 10 + d7) % 7) != 0:
                                continue
                            for d8 in range(10):
                                if d8 == d7 or d8 == d6 or d8 == d5 or d8 == d4 or d8 == d3 or d8 == d2 or d8 == d1:
                                    continue
                                if ((d6 * 100 + d7 * 10 + d8) % 11) != 0:
                                    continue
                                for d9 in range(10):
                                    if d9 == d8 or d9 == d7 or d9 == d6 or d9 == d5 or d9 == d4 or d9 == d3 or d9 == d2 or d9 == d1:
                                        continue
                                    if ((d7 * 100 + d8 * 10 + d9) % 13) != 0:
                                        continue
                                    for d10 in range(10):
                                        if d10 == d9 or d10 == d8 or d10 == d7 or d10 == d6 or d10 == d5 or d10 == d4 or d10 == d3 or d10 == d2 or d10 == d1:
                                            continue
                                        if ((d8 * 100 + d9 * 10 + d10) % 17) != 0:
                                            continue
                                        num = (d1 * 10 ** 9 + d2 * 10 ** 8 + d3 * 10 ** 7 + d4 * 10 ** 6 + d5 * 10 ** 5 +
                                               d6 * 10 ** 4 + d7 * 10 ** 3 + d8 * 10 ** 2 + d9 * 10 ** 1 + d10 * 10 ** 0)
                                        print num
                                        sum += num

print
print sum
