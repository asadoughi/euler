
map = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

def fn(i):
    if i <= 20:
        return map[i]
    elif i < 100:
        return map[i - (i%10)] + map[i%10]
    elif i < 1000:
        string = map[i / 100] + 'hundred' 
        if i % 100 > 0:
            string += 'and' + fn(i % 100)
        return string
    else:
        return 'onethousand'


total = 0
for i in range(1,1001):
    total += len(fn(i))
print total
