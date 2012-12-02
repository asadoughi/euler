
def is_palindrome(X):
    i = 0
    j = -1
    while i < len(X) + j:
        if X[i] != X[j]:
            return False
        i += 1
        j -= 1
    return True

total = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        total += i
print total

