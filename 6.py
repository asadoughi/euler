#!/usr/bin/env python

sum_squares = sum([i*i for i in range(101)])
sum = sum(range(101))
square_sum = sum * sum
print square_sum - sum_squares
