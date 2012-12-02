
def score(word):
    score = 0
    for letter in word:
        score += ord(letter) - ord('A') + 1
    return score

def triangle(max):
    n = 0
    i = 1
    triangle = []
    while n < max:
        n = i * (i+1) / 2
        triangle.append(n)
        i += 1
    return triangle

f = open('words.txt')
words = f.readline()
words = words.strip().replace('"','')
words = words.split(',')
scores = [score(word) for word in words]
tri = set(triangle(max(scores)))

count = 0
for score in scores:
    if score in tri:
        count += 1
print count

