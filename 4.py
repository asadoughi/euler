#!/usr/bin/env python

# could have used more int-based methods, but str is faster
def is_palindrome(x):
    X = str(x)
    i = 0
    j = -1
    while i < len(X) + j:
        if X[i] != X[j]:
            return False
        i += 1
        j -= 1
    return True

palindromes = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if is_palindrome(i*j):
            palindromes.append(i*j)
print max(palindromes)
